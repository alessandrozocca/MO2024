from itertools import product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_instance(x, y, **kwargs):
    """
    Generates a random instance of grid size (x, y) with a fixed seed.
    """
    coords = np.array(list(product(range(x), range(y))))

    data = {
        "n_sites": x * y,
        "coords": coords,
        "production": 150,
        "min_distance": kwargs.get("min_distance", 1.25),
        "min_turbines": kwargs.get("min_turbines", 3),
        "max_turbines": 8,
    }

    return data


def compute_interferences(coords, wind_vector):
    """
    Computes the interference matrix.
    """
    size = len(coords)
    interferences = np.zeros((size, size))

    # For every two points that do not have the same coordinates, compute the interference
    for i, coord_i in enumerate(coords):
        for j, coord_j in enumerate(coords):
            if np.any(coord_i != coord_j):
                d_ij = coord_i - coord_j

                projection = 20 * np.dot(d_ij, wind_vector)
                strength = np.linalg.norm(projection) / np.linalg.norm(d_ij) ** 2

                if projection > 0:
                    interferences[i, j] = strength

    return interferences


def sample_wind_vector(seed):
    """
    Samples a random wind vector.
    """
    rng = np.random.default_rng(seed)

    target_angle = 0.4
    width = 0.65
    angle = np.pi * rng.uniform(target_angle - width, target_angle + width)
    wind_direction = np.array([np.cos(angle), np.sin(angle)])
    wind_speed = 33 * rng.uniform() * max(np.cos(angle - target_angle), 0)

    return wind_direction * wind_speed
    

def generate_wind_farm_data(n_samples=45, x=6, y=6, seed=0):
    """
    Computes all data needed for the wind farm part of the assignment.
    """
    grid_x = x
    grid_y = y

    n_locations = grid_x * grid_y
    instance = generate_instance(grid_x, grid_y)

    samples = n_samples
    wind_vectors = np.zeros((samples, 2))
    interference_matrices = np.zeros((samples, n_locations, n_locations))

    for idx in range(samples):
        wind_vectors[idx] = sample_wind_vector(seed * n_samples + idx)
        interference_matrices[idx] = compute_interferences(
            instance["coords"], wind_vectors[idx]
        )

    return instance, interference_matrices
