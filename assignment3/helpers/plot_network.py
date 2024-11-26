from itertools import cycle

import osmnx
from matplotlib.colors import TABLEAU_COLORS


def plot_network(graph, *routes):
    """Plot a network instance, optionally including one or more routes."""
    if len(routes) == 0:
        osmnx.plot_graph(graph)
    elif len(routes) == 1:
        osmnx.plot_graph_route(graph, routes[0])
    else:
        cmap = cycle(TABLEAU_COLORS.keys())
        colors = [c for _, c in zip(routes, cmap)]
        osmnx.plot_graph_routes(graph, routes, route_colors=colors)
