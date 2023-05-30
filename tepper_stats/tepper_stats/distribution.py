import scipy as sc

from fitter import Fitter


def select(
    data,
    distributions=["norm", "uniform", "t", "skewnorm", "weibull_min", "gamma", "lognorm", "exp"],
    num_best_fit=3
):
    """Tests data against multiple distributions to determine the one with the best
    fit and returns the results

    :param data: A 1D array of data
    :param distributions: list of distributions to test, to use all 80 possible
    distributions set distributions to `None`.
    :param num_best_fit: number of best fitting distributions to show in result
    :return: (dict) distribution name with value containing parameters
    to create random sample using scipy. Ex:
    {"norm": {"scale": 1, "loc": 1}}
    """
    f = Fitter(data)
    if distributions is not None:
        f.distributions = distributions
    f.fit()
    f.summary(Nbest=num_best_fit)
    _print_instructions(f.get_best())
    return f.get_best()


def fit(data, dist_name: str):
    """Tests data against the specific distribution name provided and returns
    the results

    :param data: A 1D array of data
    :param dist_name: name of distribution to test against
    :return: (dict) distribution name with value containing parameters
    to create random sample using scipy. Ex:
    {"norm": {"scale": 1, "loc": 1}}
    """
    f = Fitter(data, distributions=[dist_name])
    f.fit()
    f.summary()
    _print_instructions(f.get_best())
    return f.get_best()


def create(num_samples, best_fit: dict):
    """Creates a new random sample based on the results of functions
    tepper_stats.distribution.create or tepper_stats.distribution.fit

    :param num_samples: number of new samples to create
    :param best_fit: result of `create` or `fit` functions
    :return: new random sample based on provided distribution and parameters
    """
    dist = list(best_fit.keys())[0]
    params = best_fit.get(dist)
    dist_func = getattr(sc.stats, dist)
    return dist_func.rvs(size=num_samples, **params)


def _print_instructions(result):
    dist = list(result.keys())[0]
    params = result.get(dist)
    print("Best Distribution Fit:")
    print(f"{dist}")
    print("Parmameters:")
    print(f"{params}")
    print("Usage:\n")
    print(f"import scipy as sc\n\n")
    print(f"params = result_from_this_function.get(\"{dist}\")")
    print(f"sample = sc.stats.{dist}.rvs(size=1000, **params)")
