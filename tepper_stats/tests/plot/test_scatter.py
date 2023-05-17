import numpy as np
import statsmodels.api as sm

from tepper_stats import plot


def test_actual_fitted(refrigerator_data):
    # Given
    df = refrigerator_data
    subset = df[["COOLSIZE", "OPCOST", "SHELVES", "FREZSIZE", "PRICE"]]
    exog = sm.add_constant(df[["COOLSIZE", "OPCOST", "SHELVES", "FREZSIZE"]])
    refrig_reg = sm.OLS(df["PRICE"], exog).fit()

    # When
    plot.actual_fitted(refrig_reg, subset, "PRICE")

    # Then
    # No exception


def test_log_actual_fitted(refrigerator_data):
    # Given
    df = refrigerator_data
    df["log_price"] = df["PRICE"].apply(lambda x: np.log(x))
    df["log_opcost"] = df["OPCOST"].apply(lambda x: np.log(x))
    subset = df[["COOLSIZE", "log_opcost", "SHELVES", "FREZSIZE", "PRICE"]]
    exog = sm.add_constant(df[["COOLSIZE", "log_opcost", "SHELVES", "FREZSIZE"]])
    refrig_reg = sm.OLS(df["log_price"], exog).fit()

    # When
    plot.log_actual_fitted(refrig_reg, subset, "PRICE")

    # Then
    # No exception


def test_objective_function():
    # Given
    def my_func(x):
        return x + 1

    # When
    plot.objective_function(my_func, range(1, 10))

    # Then
    # No exception
