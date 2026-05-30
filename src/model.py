import numpy as np

def simple_predict(cpu_usage):
    # dummy prediction: slightly smoothed version
    return np.mean(cpu_usage) * np.ones_like(cpu_usage)
