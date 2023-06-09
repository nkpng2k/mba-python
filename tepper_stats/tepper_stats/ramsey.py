import statsmodels.stats.diagnostic as smd


def ramsey_test(fitted_model):
    """
    Performs a Ramsey RESET Test on the provided fitted model. Results are expected
    to be the same as using R package lmtest::resettest

    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :return: results of statsmodel linear_reset().
    """
    one_fitted = smd.linear_reset(fitted_model, power=2, test_type="fitted", use_f=True)
    two_fitted = smd.linear_reset(fitted_model, power=[2, 3], test_type="fitted", use_f=True)

    print("One Fitted:")
    print(one_fitted.summary())
    print("Two Fitted:")
    print(two_fitted.summary())

    return one_fitted, two_fitted
