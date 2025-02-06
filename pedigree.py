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

pedigree_data = {
    clone_node: {"position": (1, 2)},
    male_node: {"position": (2, 3)},
    female_node: {"position": (2, 1)},
}

edges = [
    (male_node, clone_node), 
    (female_node, clone_node)
]

def generate_pedigree_image():
    G = nx.Graph()
    G.add_edges_from(edges)

    plt.figure(figsize=(6, 4), dpi=100)
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

save_dir = "static/pedigree"
os.makedirs(save_dir, exist_ok=True)
filename = args.clone + ".png"
save_path = os.path.join(save_dir, filename)

if __name__ == "__main__":
    with open(save_path, "wb") as f:
        f.write(generate_pedigree_image().getvalue())
    print(f"✅ Pedigree image generated: {save_path}")
