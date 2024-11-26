import networkx as nx


def get_distances_to(graph, node):
    return nx.single_source_dijkstra_path_length(graph, node, weight="length")
