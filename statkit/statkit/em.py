import numpy as np
from scipy.stats import norm


def em_gmm(data: np.ndarray, n_components: int = 2, n_iterations: int = 100, seed: int = 0) -> dict:
    """
    Fit a Gaussian Mixture Model using the EM algorithm.

    Args:
        data: 1D array of observed data
        n_components: number of Gaussian components
        n_iterations: maximum number of EM iterations
        seed: random seed for initialization

    Returns:
        Dictionary with keys: mu, sigma, pi, log_likelihoods, n_iterations
    """
    rng = np.random.default_rng(seed)
    n = len(data)
    K = n_components

    mu    = rng.choice(data, size=K, replace=False)
    sigma = np.full(K, data.std())
    pi    = np.full(K, 1.0 / K)
    log_likelihoods = []

    for iteration in range(n_iterations):
        r = np.zeros((K, n))
        for k in range(K):
            r[k] = pi[k] * norm.pdf(data, mu[k], sigma[k])
        r_sum = r.sum(axis=0)
        r /= r_sum

        log_likelihoods.append(np.log(r_sum).sum())

        N_k = r.sum(axis=1)
        mu  = (r * data).sum(axis=1) / N_k
        for k in range(K):
            diff = data - mu[k]
            sigma[k] = np.sqrt((r[k] * diff ** 2).sum() / N_k[k])
        pi = N_k / n

        if iteration > 0 and abs(log_likelihoods[-1] - log_likelihoods[-2]) < 1e-6:
            break

    return {
        'mu':              mu,
        'sigma':           sigma,
        'pi':              pi,
        'log_likelihoods': log_likelihoods,
        'n_iterations':    iteration + 1,
    }
