from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tepper_stats.tepper_stats.confidence_intervals as ci


def histogram(
        data: Union[np.ndarray, pd.DataFrame, pd.Series] = None,
        alpha: float = None,
        bins: Union[str, int] = "auto",
        title: str = "Histogram",
        x_label: str = "Frequency",
        y_label: str = "Value",
):
    """
    Displays a histogram and calculates the confidence interval
    for the data provided.

    :param data: a 1D array or array-like object.
    :param alpha: significance level to use for the confidence interval.
    :param bins: number of bins for the histogram.
    :param title: title for the histogram.
    :param x_label: label for the x-axis.
    :param y_label: label for the y-axis.
    :return:
    """
    if data.ndim != 1:
        raise ValueError("Input data array must be 1D.")

    n, bins, patches = plt.hist(x=data, bins=bins)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    max_freq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(max_freq / 10) * 10 if max_freq % 10 else max_freq + 10)
    avg = np.round(np.mean(data), 2)
    plt.axvline(avg, color="red", linestyle="--")
    plt.text(avg + 0.1, 0, f"mean={avg}", color="red")

    if alpha:
        high, low = ci.calculate_confidence_interval(data, alpha)
        plt.axvline(high, color="red")
        plt.text(high + 0.1, 0, f"{high}", color="red")
        plt.axvline(low, color="red")
        plt.text(low + 0.1, 0, f"{low}", color="red")

    plt.show()
