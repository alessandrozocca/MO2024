import networkx as nx


def make_instance(graph):
    """Create a single shortest path routing instance from a given graph.
    Returns a list of nodes and a dictionary of edges and their distances."""
    nodes = list(graph.nodes)
    edges = nx.get_edge_attributes(nx.DiGraph(graph), "length")

    pred = {i: [j for j in nodes if (j, i) in edges] for i in nodes}
    succ = {i: [j for j in nodes if (i, j) in edges] for i in nodes}

    return nodes, edges, pred, succ
