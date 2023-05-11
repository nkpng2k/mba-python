from typing import Union

import matplotlib as plt
import numpy as np
import pandas as pd


def histogram(data: Union[np.ndarray, pd.DataFrame, pd.Series] = None):
    if data.ndim != 1:
        raise ValueError("Input data array must be 1D.")
