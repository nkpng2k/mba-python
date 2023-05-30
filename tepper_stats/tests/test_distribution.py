import math

import numpy as np
import scipy as sc

from tepper_stats import distribution


def test_select():
    # Given
    gamma_dist = sc.stats.gamma.rvs(2, loc=1.5, scale=2, size=1000)

    # When
    result = distribution.select(gamma_dist)

    # Then
    dist = list(result.keys())[0]
    assert dist == "gamma"
    params = result.get(dist)
    assert math.isclose(params["scale"], 2, rel_tol=0.5)
    assert math.isclose(params["a"], 2, rel_tol=0.5)
    assert math.isclose(params["loc"], 1.5, rel_tol=0.5)


def test_fit():
    # Given
    gamma_dist = sc.stats.gamma.rvs(2, loc=1.5, scale=2, size=1000)

    # When
    result = distribution.fit(gamma_dist, "gamma")

    # Then
    dist = list(result.keys())[0]
    assert dist == "gamma"
    params = result.get(dist)
    assert math.isclose(params["scale"], 2, rel_tol=0.5)
    assert math.isclose(params["a"], 2, rel_tol=0.5)
    assert math.isclose(params["loc"], 1.5, rel_tol=0.5)


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
    scale = np.random.randint(0, 10)
    loc = np.random.randint(0, 10)
    num_samples = np.random.randint(100, 1000)
    norm_dist = sc.stats.norm.rvs(size=100, scale=scale, loc=loc)
    result = distribution.fit(norm_dist, "norm")

    # When
    sample = distribution.create(num_samples, result)

    # Then
    assert len(sample) == num_samples
