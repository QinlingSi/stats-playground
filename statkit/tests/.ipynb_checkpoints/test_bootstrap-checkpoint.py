import numpy as np
from statkit.bootstrap import bootstrap_statistic, bootstrap_ci


rng = np.random.default_rng(0)
DATA = rng.exponential(50, 200)


def test_bootstrap_statistic_shape():
    estimates = bootstrap_statistic(DATA, np.mean, n_iterations=1000)
    assert estimates.shape == (1000,)


def test_bootstrap_statistic_reproducible():
    est1 = bootstrap_statistic(DATA, np.mean, seed=1)
    est2 = bootstrap_statistic(DATA, np.mean, seed=1)
    assert np.allclose(est1, est2)


def test_bootstrap_ci_contains_mean():
    lo, hi = bootstrap_ci(DATA, np.mean)
    assert lo < DATA.mean() < hi


def test_bootstrap_ci_width():
    lo, hi = bootstrap_ci(DATA, np.mean, confidence=0.95)
    assert hi - lo > 0


def test_bootstrap_ci_median():
    lo, hi = bootstrap_ci(DATA, np.median)
    assert lo < np.median(DATA) < hi
