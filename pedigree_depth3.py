import matplotlib.pyplot as plt
import networkx as nx
import io
import os
import argparse

parser = argparse.ArgumentParser(description='Pedigree drawing')
parser.add_argument('--clone', '-c', type=str, required=True, help='Clone name')
parser.add_argument('--male', '-m', type=str, required=True, help='Parent male name')
parser.add_argument('--female', '-f', type=str, required=True, help='Parent female name')
args = parser.parse_args()

clone_node = args.clone + '_clone'
male_node = args.male + '_male'
female_node = args.female + '_female'
male_male_node = 'male1_male_male'
male_female_node = 'female1_male_female'
female_male_node = 'male2_female_male'
female_female_node = 'female2_female_female'

pedigree_data = {
    "clone": {"position": (1, 8)},
    "male": {"position": (2, 13)},
    "female": {"position": (2, 4)},
    "male_male": {"position": (3, 14)},
    "male_female": {"position": (3, 10)},
    "female_male": {"position": (3, 6)},
    "female_female": {"position": (3, 2)},
    "male_male_male": {"position": (4, 15)},
    "male_male_female": {"position": (4, 13)},
    "male_female_male": {"position": (4, 11)},
    "male_female_female": {"position": (4, 9)},
    "female_male_male": {"position": (4, 7)},
    "female_male_female": {"position": (4, 5)},
    "female_female_male": {"position": (4, 3)},
    "female_female_female": {"position": (4, 1)}
}

edges = [
    ("clone", "male"),
    ("clone", "female"),
    ("male", "male_male"),
    ("male", "male_female"),
    ("female", "female_male"),
    ("female", "female_female"),
    ("male_male", "male_male_male"),
    ("male_male", "male_male_female"),
    ("male_female", "male_female_male"),
    ("male_female", "male_female_female"),
    ("female_male", "female_male_male"),
    ("female_male", "female_male_female"),
    ("female_female", "female_female_male"),
    ("female_female", "female_female_female")
]

def generate_pedigree_image():
    G = nx.Graph()
    G.add_edges_from(edges)

    plt.figure(figsize=(8, 5), dpi=100)
    pos = {node: data["position"] for node, data in pedigree_data.items()}
    nx.draw_networkx_edges(G, pos, edge_color="black")

    for node, (x, y) in pos.items():
        clean_label = node.replace("_male", "").replace("_female", "").replace("_clone", "")
        plt.text(
            x, y, clean_label, fontsize=12, ha="center", va="center", fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3")
        )

    plt.axis("off")

    img = io.BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    return img

save_dir = ""
filename = args.clone + ".png"
save_path = os.path.join(save_dir, filename)

if __name__ == "__main__":
    with open(save_path, "wb") as f:
        f.write(generate_pedigree_image().getvalue())
    print(f"✅ Pedigree image generated: {save_path}")
