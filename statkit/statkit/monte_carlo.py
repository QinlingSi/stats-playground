import numpy as np


def monte_carlo_pi(n_samples: int, seed: int = 42) -> float:
    """
    Estimate pi using the Monte Carlo method.

    Args:
        n_samples: number of random points to generate
        seed: random seed for reproducibility

    Returns:
        Estimated value of pi
    """
    rng = np.random.default_rng(seed)
    x = rng.random(n_samples)
    y = rng.random(n_samples)
    inside = ((x - 0.5) ** 2 + (y - 0.5) ** 2) <= 0.25
    return 4 * inside.sum() / n_samples


def monte_carlo_integral(func, a: float, b: float, n_samples: int = 100_000, seed: int = 42) -> float:
    """
    Estimate a definite integral using Monte Carlo sampling.

    Args:
        func: callable, the function to integrate
        a: lower bound of integration
        b: upper bound of integration
        n_samples: number of random samples
        seed: random seed for reproducibility

    Returns:
        Estimated value of the integral
    """
    rng = np.random.default_rng(seed)
    x = rng.uniform(a, b, n_samples)
    return (b - a) * np.mean(func(x))
