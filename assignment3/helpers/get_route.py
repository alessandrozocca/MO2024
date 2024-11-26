def get_route(model):
    route = [model.s()]
    while route[-1] != model.t():
        route.append(
            max(
                model.nodes,
                key=lambda i: (
                    model.x[route[-1], i]() if (route[-1], i) in model.edges else -1
                ),
            )
        )
    return route
