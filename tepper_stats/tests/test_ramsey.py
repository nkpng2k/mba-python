import statsmodels.api as sm

from tepper_stats import ramsey


def test_ramsey(refrigerator_data):
    # Given
    df = refrigerator_data
    exog = sm.add_constant(df[["COOLSIZE", "OPCOST", "SHELVES", "FREZSIZE"]])
    reg = sm.OLS(df["PRICE"], exog)
    reg_result = reg.fit()

    # NOTE: work around due to https://github.com/statsmodels/statsmodels/issues/8879
    reg_np = sm.OLS(reg_result.model.endog, reg_result.model.exog).fit()

    # When
    ramsey_result = ramsey.ramsey_test(reg_np)

    # Then
    assert ramsey_result[0].pvalue == 4.5241990720571154e-07
    assert ramsey_result[1].pvalue == 3.295179553275511e-06
