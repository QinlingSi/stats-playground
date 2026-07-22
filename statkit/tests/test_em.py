import numpy as np
from statkit.em import em_gmm


rng = np.random.default_rng(42)
DATA = np.concatenate([
    rng.normal(0, 1, 300),
    rng.normal(5, 1, 300)
])


def test_em_returns_correct_keys():
    result = em_gmm(DATA, n_components=2)
    assert set(result.keys()) == {'mu', 'sigma', 'pi', 'log_likelihoods', 'n_iterations'}


def test_em_n_components():
    result = em_gmm(DATA, n_components=2)
    assert len(result['mu']) == 2
    assert len(result['sigma']) == 2
    assert len(result['pi']) == 2


def test_em_pi_sums_to_one():
    result = em_gmm(DATA, n_components=2)
    assert abs(result['pi'].sum() - 1.0) < 1e-6


def test_em_log_likelihood_increases():
    result = em_gmm(DATA, n_components=2)
    lls = result['log_likelihoods']
    for i in range(1, len(lls)):
        assert lls[i] >= lls[i-1] - 1e-6


def test_em_recovers_means():
    result = em_gmm(DATA, n_components=2)
    estimated_means = sorted(result['mu'])
    assert abs(estimated_means[0] - 0) < 0.5
    assert abs(estimated_means[1] - 5) < 0.5
