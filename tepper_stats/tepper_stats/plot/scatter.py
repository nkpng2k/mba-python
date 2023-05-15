from typing import Callable
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def actual_fitted():
    pass


def log_actual_fitted():
    pass


def objective_function(fn: Callable, vector: Sequence):
    df = pd.DataFrame(vector, columns=["x_var"])
    df["y_var"] = df["x_var"].apply(lambda x: np.mean(fn(x)))

    plt.scatter(df["x_var"], df["y_var"])
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Objective Function Plot")
    plt.show()
