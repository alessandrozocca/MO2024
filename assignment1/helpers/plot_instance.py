import folium


def plot_instance(
    data,
    plot_edges: bool = False,
    solution: list[str] | None = None,
):
    """
    Plots the Tour du Mont Blanc problem instance.

    Parameters
    ----------
    data
        The data for the Tour du Mont Blanc problem.
    plot_edges
        Whether to plot the edges of the graph.
    solution
        A solution, consisting of the sequence of huts to visit in order.
    """
    center = (45.879781359601424, 6.9462292487021715)
    map = folium.Map(location=center, zoom_start=10, width=900, height=900)

    for node in data.nodes:
        folium.Marker(
            location=data.coords[node],
            popup=node,
            icon=folium.Icon(icon="home", prefix="fa"),
        ).add_to(map)

    if plot_edges:
        for frm, to in data.edges:
            from_lat, from_long = data.coords[frm]
            to_lat, to_long = data.coords[to]

            folium.PolyLine(
                locations=[(from_lat, from_long), (to_lat, to_long)],
                color="black",
                weight=1,
                opacity=0.7,
                arrow_head=True,
            ).add_to(map)

    if solution:
        edges = list(zip(solution[:-1], solution[1:]))

        for frm, to in edges:
            from_lat, from_long = data.coords[frm]
            to_lat, to_long = data.coords[to]

            folium.PolyLine(
                locations=[(from_lat, from_long), (to_lat, to_long)],
                color="blue",
                weight=3,
                opacity=0.7,
            ).add_to(map)

    return map
