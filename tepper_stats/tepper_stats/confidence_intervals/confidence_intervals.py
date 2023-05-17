import numpy as np


def calculate_confidence_interval(data, alpha=0.1):
    """
    Calculates the confidence interval for the provided data based on
    the provided significance level

    :param data: 1-D DataFrame or numpy array
    :param alpha: the significance level to create
    the confidence interval on
    :return: the upper and lower bounds of the
    confidence interval for the provided data
    """
    high = round(np.quantile(data, alpha/2), 2)
    low = round(np.quantile(data, 1-alpha/2), 2)

    return high, low
