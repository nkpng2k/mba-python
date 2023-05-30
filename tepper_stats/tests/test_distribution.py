import math

import numpy as np
import scipy as sc

from tepper_stats import distribution


def test_select():
    # Given
    sknorm_dist = sc.stats.skewnorm.rvs(2, loc=1.5, scale=2, size=3000)

    # When
    result = distribution.select(
        sknorm_dist,
        distributions=["norm", "skewnorm", "gamma", "exp", "uniform"]
    )

    # Then
    dist = list(result.keys())[0]
    assert dist == "skewnorm"
    params = result.get(dist)
    assert math.isclose(params["a"], 2, rel_tol=0.2)
    assert math.isclose(params["scale"], 2, rel_tol=0.2)
    assert math.isclose(params["loc"], 1.5, rel_tol=0.2)


def test_fit():
    # Given
    norm_dist = sc.stats.norm.rvs(loc=1.5, scale=2, size=1000)

    # When
    result = distribution.fit(norm_dist, "norm")

    # Then
    dist = list(result.keys())[0]
    assert dist == "norm"
    params = result.get(dist)
    assert math.isclose(params["scale"], 2, rel_tol=0.2)
    assert math.isclose(params["loc"], 1.5, rel_tol=0.2)


def test_fit_different_distribution():
    # Given
    scale = np.random.randint(0, 10)
    loc = np.random.randint(0, 10)
    norm_dist = sc.stats.norm.rvs(size=1000, scale=scale, loc=loc)

    # When
    result = distribution.fit(norm_dist, "uniform")

    # Then
    dist = list(result.keys())[0]
    assert dist == "uniform"


def test_create():
    # Given
    num_samples = np.random.randint(100, 1000)
    norm_dist = sc.stats.norm.rvs(size=100, scale=1.5, loc=2)
    result = distribution.fit(norm_dist, "norm")

    # When
    sample = distribution.create(num_samples, result)

    # Then
    assert len(sample) == num_samples
