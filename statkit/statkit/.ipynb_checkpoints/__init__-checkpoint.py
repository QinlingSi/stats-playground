"""
statkit: A lightweight statistical toolkit.

Modules:
    monte_carlo: Monte Carlo simulation methods
    bootstrap:   Bootstrap resampling and confidence intervals
    em:          EM algorithm for Gaussian Mixture Models
"""

from .monte_carlo import monte_carlo_pi, monte_carlo_integral
from .bootstrap   import bootstrap_statistic, bootstrap_ci
from .em          import em_gmm

__version__ = '0.1.0'
__author__  = 'Your Name'
