import numpy as np


def calculate_confidence_interval(data, alpha=0.1):
    high = round(np.quantile(data, alpha/2), 2)
    low = round(np.quantile(data, 1-alpha/2), 2)

    return high, low
