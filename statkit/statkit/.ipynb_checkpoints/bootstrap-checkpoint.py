import numpy as np


def bootstrap_statistic(data: np.ndarray, statistic_func, n_iterations: int = 10_000, seed: int = 42) -> np.ndarray:
    """
    Estimate the sampling distribution of a statistic via Bootstrap resampling.

    Args:
        data: 1D array of observed sample data
        statistic_func: function that takes an array and returns a scalar
        n_iterations: number of bootstrap resamples
        seed: random seed for reproducibility

    Returns:
        Array of bootstrap estimates
    """
    rng = np.random.default_rng(seed)
    n = len(data)
    estimates = np.empty(n_iterations)
    for i in range(n_iterations):
        resample = rng.choice(data, size=n, replace=True)
        estimates[i] = statistic_func(resample)
    return estimates


def bootstrap_ci(data: np.ndarray, statistic_func, confidence: float = 0.95, n_iterations: int = 10_000, seed: int = 42) -> tuple:
    """
    Compute a Bootstrap confidence interval for a statistic.

    Args:
        data: 1D array of observed sample data
        statistic_func: function that takes an array and returns a scalar
        confidence: confidence level (default 0.95)
        n_iterations: number of bootstrap resamples
        seed: random seed for reproducibility

    Returns:
        Tuple (lower, upper) representing the confidence interval
    """
    estimates = bootstrap_statistic(data, statistic_func, n_iterations, seed)
    alpha = 1 - confidence
    lower = np.percentile(estimates, 100 * alpha / 2)
    upper = np.percentile(estimates, 100 * (1 - alpha / 2))
    return lower, upper
