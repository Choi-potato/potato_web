from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from markupsafe import escape
import os
from PIL import Image
from rembg import remove
from werkzeug.utils import secure_filename
import uuid
import json
from flask_caching import Cache

app = Flask(__name__)

app.config["CACHE_TYPE"] = "simple"
cache = Cache(app)

UPLOAD_FOLDER = "img/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@cache.memoize(timeout=300)
def load_cultivars_info():
    with open("cultivars_info.json", "r", encoding="utf-8") as file:
        return json.load(file)

#remove background image and convert to RGBA(Red Green Blue Alpha)
def remove_background_from_disk(file_path):
    with open(file_path, "rb") as file:
        input_image = file.read()
    output_image = remove(input_image)
    processed_image = Image.open(BytesIO(output_image)).convert("RGBA")
    processed_path = os.path.join(UPLOAD_FOLDER, "processed_" + os.path.basename(file_path))
    processed_image.save(processed_path, format="PNG")
    return processed_path, processed_image

#Extract RGB value
def extract_rgb(image):
    width, height = image.size
    rgb_values = []
    for x in range(width):
        for y in range(height):
            r, g, b, a = image.getpixel((x, y))
            if a > 0:
                rgb_values.append((r, g, b))
    return np.array(rgb_values)

def plot_histogram_and_find_mode(rgb_array):
    plt.figure(figsize=(4, 4))
    mode_values = {}
    for i, color in enumerate(['Red', 'Green', 'Blue']):
        counts, bins = np.histogram(rgb_array[:, i], bins=256, range=(0, 255))
        mode_value = bins[np.argmax(counts)]
        mode_values[color] = int(mode_value)
        plt.hist(rgb_array[:, i], bins=256, color=color.lower(), alpha=0.6, label=f"{color} (Mode: {int(mode_value)})")
    plt.xlabel('Color Value: 0 to 255')
    plt.ylabel('Frequency')
    plt.legend()
    hist_io = BytesIO()
    plt.savefig(hist_io, format="png", bbox_inches='tight')
    plt.close(fig)
    hist_io.seek(0)
    hist_base64 = base64.b64encode(hist_io.read()).decode("utf-8")
    hist_io.close()
    return f"data:image/png;base64,{hist_base64}", mode_values

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/cultivar_list')
def cultivar_list():
    return render_template('cultivar_list.html')

@app.route('/flesh_color')
def flesh_color():
    return render_template('flesh_color.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = escape(request.form.get('name', '').strip().lower())

    if not search_query:
        return redirect(url_for('home'))

    if search_query in search_mapping:
        return redirect(url_for('results', query=search_mapping[search_query]))

    matched_cultivars = [search_mapping[key] for key in search_mapping if search_query in key.lower()]
    matching_cultivars = []
    for each in matched_cultivars:
        if each not in matching_cultivars:
            matching_cultivars.append(each)
    matched_cultivars = matching_cultivars


    if not matched_cultivars:
        return redirect(url_for('no_results'))

    return redirect(url_for('results', query=",".join(matched_cultivars)))

@app.route('/results')
def results():
    query = request.args.get('query', '')
    cultivar_keys = query.split(",")
    cultivar_data_list = [cultivars_info.get(key) for key in cultivar_keys if key in cultivars_info]
    if not cultivar_data_list:
        return redirect(url_for('no_results'))

    return render_template('search_results.html', cultivars=cultivar_data_list)

@app.route('/no_results')
def no_results():
    return render_template('no_results.html')

@app.route('/cultivar/<name>')
def cultivar_detail(name):
    name = name.lower()
    if name in search_mapping:
        name = search_mapping[name]
    cultivar_data = cultivars_info.get(name)
    if not cultivar_data:
        return redirect(url_for('no_results'))
    return render_template('cultivar_detail.html', cultivar=cultivar_data)

@app.route('/cultivar/<name>/<int:depth>')
def cultivar_depth_detail(name, depth):
    name = name.lower()
    if name in search_mapping:
        name = search_mapping[name]
    cultivar_data = cultivars_info.get(name)
    if not cultivar_data:
        return redirect(url_for('no_results'))
    elif depth == 1:
        return render_template('cultivar_detail.html', cultivar=cultivar_data)
    return render_template(f'cultivar_detail{depth}.html', cultivar=cultivar_data)

@app.route('/upload', methods=['POST'])
def upload_image():
    if "file" not in request.files:
        return "No file uploaded!", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    
    unique_filename = str(uuid.uuid4().hex) + '_' + secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(file_path)

    processed_path, processed_image = remove_background_from_disk(file_path)

    rgb_array = extract_rgb(processed_image)
    hist_base64, mode_values = plot_histogram_and_find_mode(rgb_array)

    with open(file_path, "rb") as original_file:
        original_base64 = base64.b64encode(original_file.read()).decode("utf-8")
    
    with open(processed_path, "rb") as processed_file:
        processed_base64 = base64.b64encode(processed_file.read()).decode("utf-8")

    processed_image.close()
    os.remove(file_path)
    os.remove(processed_path)

    return render_template('flesh_color_result.html', original_image=f"data:image/png;base64,{original_base64}", processed_image=f"data:image/png;base64,{processed_base64}", histogram=hist_base64, mode_value_rgb = mode_values)


cultivars_info = load_cultivars_info()
search_mapping = {key.lower(): key for key in cultivars_info}

for key, value in cultivars_info.items():
    search_mapping[value['korean_name']] = key

    if  'it_number' in value and value['it_number']:
        search_mapping[value['it_number'].lower()] = key

    if 'alt_english_name' in value and value['alt_english_name']:
        search_mapping[value['alt_english_name'].lower()] = key

    if 'alt_name' in value and value['alt_name']:
        search_mapping[value['alt_name']] = key

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
