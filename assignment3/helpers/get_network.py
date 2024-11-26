import osmnx


def get_network(center, radius):
    """Get a networkx MultiDiGraph object representing the area specified in the query."""
    return osmnx.graph.graph_from_address(
        center, radius, network_type="walk", simplify=True
    )
