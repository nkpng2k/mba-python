def test_h(fitted_model, conditions):
    cov_type = "HC1"
    refitted = fitted_model.get_robustcov_results(cov_type=cov_type)

    results = refitted.t_test(conditions)
    print(results)

    return results


def test_hac(fitted_model, conditions, max_lags=1):
    cov_type = "HAC"
    refitted = fitted_model.get_robustcov_results(cov_type=cov_type, maxlags=max_lags)

    results = refitted.t_test(conditions)
    print(results)

    return results
