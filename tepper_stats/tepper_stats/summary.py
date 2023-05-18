def summary_h(fitted_model):
    """
    This function displays regression results with standard errors adjusted for
    possible presence of heteroskedasticity using the method developed by White.
    This method is appropriate for cross-section data.

    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :return: refitted model with coefficients and standard error
    heteroskedasticity robustness
    """
    cov_type = "HC1"
    refitted = fitted_model.get_robustcov_results(cov_type=cov_type)

    print(refitted.summary())

    return refitted


def summary_hac(fitted_model, max_lags=1):
    """
    This function displays regression results with standard errors adjusted for
    possible presence of heteroskedasticity and autocorrelation using the
    method developed by Newey and West.
    This method is appropriate for time series data.

    :param fitted_model: a model created by `.fit()` method from statsmodel package
    :param max_lags: (default: 1) number of lags seen in data.
    :return: refitted model with coefficients and standard error
    """
    cov_type = "HAC"
    refitted = fitted_model.get_robustcov_results(cov_type=cov_type, maxlags=max_lags)

    print(refitted.summary())

    return refitted
