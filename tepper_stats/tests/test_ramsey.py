import pandas as pd
import statsmodels.api as sm

from tepper_stats import ramsey


def test_ramsey():
    # Given
    df = pd.read_excel("./data/Refrigerator_Data.xlsx")
    exog = sm.add_constant(df[["COOLSIZE", "OPCOST", "SHELVES", "FREZSIZE"]])
    reg = sm.OLS(df["PRICE"], exog)
    reg_result = reg.fit()

    # NOTE: work around due to https://github.com/statsmodels/statsmodels/issues/8879
    reg_np = sm.OLS(reg_result.model.endog, reg_result.model.exog).fit()

    # When
    ramsey_result = ramsey.ramsey_test(reg_np)

    # Then
    assert ramsey_result[0] is not None
    assert ramsey_result[1] is not None
