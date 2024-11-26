import math

import networkx as nx


def get_distances_to(graph, node):
    return nx.single_source_dijkstra_path_length(graph, node, weight="length")


def get_crowdedness(graph):
    c = 5395065019
    delta = get_distances_to(graph, c)
    return {k: 2 * math.exp(-v / 250) if k != c else 2 for k, v in delta.items()}
