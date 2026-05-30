import pandas as pd
import numpy as np

def generate_data(n=1000):
    np.random.seed(42)

    data = pd.DataFrame({
        "timestamp": pd.date_range(start="2024-01-01", periods=n, freq="H"),
        "cpu_usage": np.random.rand(n) * 100,
        "cost": np.random.rand(n) * 10,
    })

    return data
