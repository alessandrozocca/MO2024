from itertools import product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_wind_farm(instance, solution, wind=None):
    coords = instance["coords"]
    min_distance = instance["min_distance"]

    _, ax = plt.subplots(figsize=[10, 10])

    ax.scatter(coords[:, 0], coords[:, 1], s=100, label="site")

    for idx in range(len(coords)):
        margin = 0.05
        ax.annotate(idx, (coords[idx, 0] + margin, coords[idx, 1] + margin))

    turbine_coords = coords[solution]
    ax.scatter(*turbine_coords.T, s=100, label="turbine")

    for (x, y) in turbine_coords:
        cir = plt.Circle((x, y), min_distance, color="r", fill=False)
        ax.add_patch(cir)

    ax.set_xlim(coords[:, 0].min() - 1, coords[:, 0].max() + 1)
    ax.set_ylim(coords[:, 1].min() - 1, coords[:, 1].max() + 1)

    if wind is None:
        ax.set_title(f"Wind farm layout\nSelected sites: {solution}")
    else:
        ax.set_title(f"Wind farm layout for wind {wind}\nSelected sites: {solution}")
    ax.legend()
    plt.tight_layout()
    plt.show()
