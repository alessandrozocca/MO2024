from itertools import product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_economic_dispatch_data():
    nodes_df = pd.read_csv(
        "https://gist.githubusercontent.com/leonlan/8145e4477dabe97705c60aa4d55363f5/raw/6ab2d382a0634125aa25f469faa1d7a03afb8596/nodes.csv",
        index_col=0,
    )[["node_id", "d", "p_min", "p_max", "c_var"]]

    wind_production_samples_df = pd.read_csv(
        "https://gist.githubusercontent.com/leonlan/8145e4477dabe97705c60aa4d55363f5/raw/7816951386b4cdd2b624b0c4a34a6c8b66bc1dc8/discrete_wind.csv"
    ).T

    # Read data
    nodes = nodes_df.set_index("node_id").T.to_dict()
    wind_production_samples = list(wind_production_samples_df.to_dict().values())
    wind_production_samples = [sum(d.values()) for d in wind_production_samples]

    return nodes, wind_production_samples