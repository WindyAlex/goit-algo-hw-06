import networkx as nx
import matplotlib.pyplot as plt

from graph import create_graph


def main():
    G = create_graph()

    print("Graph analysis")
    print("Vertices:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())

    print("\nDegree of vertices:")
    for node in G.nodes():
        print(node, "->", G.degree(node))

    pos = nx.spring_layout(G, seed=42)

    node_colors = []
    for node in G.nodes():
        t = G.nodes[node].get("node_type", "")
        if t == "router":
            node_colors.append("lightblue")
        else:
            node_colors.append("lightgreen")

    nx.draw(G, pos, with_labels=True,
            node_color=node_colors, node_size=1800, font_size=9)
    plt.title("Internet topology: Routers + Servers")
    plt.show()


main()
