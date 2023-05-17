from typing import Callable
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


def actual_fitted(fitted_model, data: pd.DataFrame, col_name: str, alpha=0.05):
    """
    Plots the fitted values of a model for the provided data.

    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :param data: pandas DataFrame with independent and dependent variables
    :param col_name: Name of the dependent variable as a string
    :param alpha: significance level with which to generate the prediction intervals
    :return:
    """
    target = data[col_name]
    if fitted_model.k_constant != 0:
        data = sm.add_constant(data[data.columns.drop(col_name)])
    else:
        data = data[data.columns.drop(col_name)]
    predictions = fitted_model.get_prediction(data)
    pred_summary = predictions.summary_frame(alpha=alpha)

    plt.plot(pred_summary.index, pred_summary["mean"], label="Predictions", color="red")
    plt.plot(pred_summary.index, target, label="Actual Values", marker="o", color="black")
    plt.plot(pred_summary.index, pred_summary["obs_ci_lower"], label="Lower Prediction Interval", color="blue")
    plt.plot(pred_summary.index, pred_summary["obs_ci_upper"], label="Upper Prediction Interval", color="blue")
    plt.legend()
    plt.show()


def log_actual_fitted(fitted_model, data: pd.DataFrame, col_name: str, alpha=0.05):
    """
    Plots the fitted values of a model for the provided data, where the log of
    a data column was used as the dependent variable.
    Ex. dependent variable was log(PRICE) instead of PRICE.

    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :param data: pandas DataFrame with independent and dependent variables
    :param col_name: Name of the dependent variable as a string
    :param alpha: significance level with which to generate the prediction intervals
    :return:
    """
    target = data[col_name]
    if fitted_model.k_constant != 0:
        data = sm.add_constant(data[data.columns.drop(col_name)])
    else:
        data = data[data.columns.drop(col_name)]
    predictions = fitted_model.get_prediction(data)
    pred_summary = predictions.summary_frame(alpha=alpha)
    pred_summary = pred_summary.apply(lambda x: np.exp(x))

    plt.plot(pred_summary.index, pred_summary["mean"], label="Predictions", color="red")
    plt.plot(pred_summary.index, target, label="Actual Values", marker="o", color="black")
    plt.plot(pred_summary.index, pred_summary["obs_ci_lower"], label="Lower Prediction Interval", color="blue")
    plt.plot(pred_summary.index, pred_summary["obs_ci_upper"], label="Upper Prediction Interval", color="blue")
    plt.legend()
    plt.show()


def objective_function(fn: Callable, vector: Sequence):
    df = pd.DataFrame(vector, columns=["x_var"])
    df["y_var"] = df["x_var"].apply(lambda x: np.mean(fn(x)))

    plt.scatter(df["x_var"], df["y_var"])
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Objective Function Plot")
    plt.show()
