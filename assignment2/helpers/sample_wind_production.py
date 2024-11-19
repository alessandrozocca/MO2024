import numpy as np


def sample_wind_production(
    n_samples=730,
    seed=0,
    rho=0.0,
    muA=460.06,
    muB=323.18,
    sigmaA=195.61,
    sigmaB=156.46,
):
    np.random.seed(seed)

    samples = np.random.multivariate_normal(
        [muA, muB],
        [
            [sigmaA**2, rho * sigmaA * sigmaB],
            [rho * sigmaA * sigmaB, sigmaB**2],
        ],
        n_samples,
    )

    samples[samples < 0] = 0  # Replace any negative values with zeros

    windpowerA = samples[:, 0]
    windpowerB = samples[:, 1]
    wind_combined = [windpowerA[i] + windpowerB[i] for i in range(len(windpowerA))]

    return windpowerA, windpowerB, wind_combined
