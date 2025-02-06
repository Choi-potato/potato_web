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
    clone_node: {"position": (1, 4)},
    male_node: {"position": (2, 6)},
    female_node: {"position": (2, 2)},
    male_male_node: {"position": (3, 7)},
    male_female_node: {"position": (3, 5)},
    female_male_node: {"position": (3, 3)},
    female_female_node: {"position": (3, 1)}
}


edges = [
    (male_node, clone_node), 
    (female_node, clone_node),
    (male_male_node, male_node),
    (male_female_node, male_node),
    (female_male_node, female_node),
    (female_female_node, female_node)


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

save_dir = ""
filename = args.clone + ".png"
save_path = os.path.join(save_dir, filename)

if __name__ == "__main__":
    with open(save_path, "wb") as f:
        f.write(generate_pedigree_image().getvalue())
    print(f"✅ Pedigree image generated: {save_path}")
