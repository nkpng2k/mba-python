from statsmodels.stats.diagnostic import linear_reset


def ramsey_test(fitted_model):
    one_fitted = linear_reset(fitted_model, power=2, test_type="fitted", use_f=True)
    two_fitted = linear_reset(fitted_model, power=[2, 3], test_type="fitted", use_f=True)

    print("One Fitted:")
    print(one_fitted.summary())
    print("Two Fitted:")
    print(two_fitted.summary())

    return one_fitted, two_fitted
