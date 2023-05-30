def test_h(fitted_model, conditions):
    """
    Tests a linear hypothesis about coefficients. The calculation
    corrects for possible presence of heteroskedasticity using the
    method developed by White.
    This method is appropriate for cross-section data.
    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :param conditions: (String) conditions to test via hypothesis test
    Example: "PARAMETER1=PARAMETER2" or "B1=0,B1=B2"
    :return: results of hypothesis test
    """
    cov_type = "HC1"
    refitted = fitted_model.get_robustcov_results(cov_type=cov_type)

    results = refitted.t_test(conditions)
    print(results)

    return results


def test_hac(fitted_model, conditions, max_lags=1):
    """
    Tests a linear hypothesis about coefficients. The calculation
    corrects for possible presence of heteroskedasticity and
    autocorrelation using the method developed by Newey and West.
    This method is appropriate for time series data.
    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :param conditions: (String) conditions to test via hypothesis test
    Example: "PARAMETER1=PARAMETER2" or "B1=0,B1=B2"
    :param max_lags: (default: 1) number of lags seen in data.
    :return: results of hypothesis test
    """
    cov_type = "HAC"
    refitted = fitted_model.get_robustcov_results(cov_type=cov_type, maxlags=max_lags)

    results = refitted.t_test(conditions)
    print(results)

    return results
