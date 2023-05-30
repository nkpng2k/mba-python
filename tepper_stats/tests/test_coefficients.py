import numpy as np
import statsmodels.api as sm

from tepper_stats import coefficients


def test_coefficients_test_h(refrigerator_data):
    # Given
    df = refrigerator_data
    exog = sm.add_constant(df[["COOLSIZE", "OPCOST", "SHELVES", "FREZSIZE"]])
    refrig_reg = sm.OLS(df["PRICE"], exog).fit()

    # When
    result = coefficients.test_h(refrig_reg, "OPCOST=COOLSIZE")

    # Then
    # No Exceptions


def test_coefficients_test_hac(beer_data):
    # Given
    df = beer_data
    df["BeerPerCapLog"] = df["BeerPerCap"].apply(lambda x: np.log(x))
    df["RealPbeerLog"] = df["RealPbeer"].apply(lambda x: np.log(x))
    df["RealPcincLog"] = df["RealPcinc"].apply(lambda x: np.log(x))
    df["BeerPerCapLogLag"] = df["BeerPerCapLog"].shift(1)
    exog = sm.add_constant(df[["RealPbeerLog", "RealPcincLog", "BeerPerCapLogLag"]])
    beer_reg = sm.OLS(df["BeerPerCapLog"], exog, missing="drop").fit()

    # When
    result = coefficients.test_hac(beer_reg, "RealPbeerLog=RealPcincLog")

    # Then
    # No Exceptions
