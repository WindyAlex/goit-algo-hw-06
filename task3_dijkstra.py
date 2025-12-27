import networkx as nx

from graph import create_weighted_graph


def main():
    G = create_weighted_graph()

    print("Task 3: Dijkstra shortest paths (by weight)\n")

    nodes = list(G.nodes())

    for start in nodes:
        lengths, paths = nx.single_source_dijkstra(G, start, weight="weight")
        print("From:", start)
        for target in nodes:
            if target == start:
                continue
            print("  to", target, "| cost =", lengths[target],
                  "| path =", paths[target])
        print()


main()
