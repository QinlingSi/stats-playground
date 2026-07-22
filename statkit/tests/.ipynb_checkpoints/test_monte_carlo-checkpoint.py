import numpy as np
from statkit.monte_carlo import monte_carlo_pi, monte_carlo_integral


def test_monte_carlo_pi_close_to_true():
    est = monte_carlo_pi(100_000)
    assert abs(est - np.pi) < 0.05


def test_monte_carlo_pi_reproducible():
    est1 = monte_carlo_pi(10_000, seed=1)
    est2 = monte_carlo_pi(10_000, seed=1)
    assert est1 == est2


def test_monte_carlo_pi_different_seeds():
    est1 = monte_carlo_pi(10_000, seed=1)
    est2 = monte_carlo_pi(10_000, seed=2)
    assert est1 != est2


def test_monte_carlo_integral_sin():
    est = monte_carlo_integral(np.sin, 0, np.pi, n_samples=100_000)
    assert abs(est - 2.0) < 0.05


def test_monte_carlo_integral_constant():
    est = monte_carlo_integral(lambda x: np.ones_like(x), 0, 5, n_samples=10_000)
    assert abs(est - 5.0) < 0.01
