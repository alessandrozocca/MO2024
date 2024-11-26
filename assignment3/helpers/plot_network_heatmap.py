import osmnx


def plot_network_heatmap(
    graph, route=None, node_color=None, edge_color=None, route_color=None
):
    """Plot a network instance, optionally including one or more routes."""
    if route is None:
        osmnx.plot_graph(graph, node_color=node_color, edge_color=edge_color)
    else:
        osmnx.plot_graph_route(
            graph,
            route,
            node_color=node_color,
            edge_color=edge_color,
            route_color=route_color,
        )
