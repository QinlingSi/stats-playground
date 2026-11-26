# statkit

A lightweight statistical toolkit built from scratch in Python.

## Installation

From the root of this repository:

```bash
pip install -e ./statkit
```

Run the tests:

```bash
pytest statkit/tests
```

## Modules

### Monte Carlo

```python
from statkit.monte_carlo import monte_carlo_pi, monte_carlo_integral
import numpy as np

est = monte_carlo_pi(100_000)
print(f'pi ≈ {est:.5f}')

est = monte_carlo_integral(np.sin, 0, np.pi)
print(f'integral of sin(x) from 0 to pi ≈ {est:.5f}')
```

### Bootstrap

```python
from statkit.bootstrap import bootstrap_statistic, bootstrap_ci
import numpy as np

data = np.random.default_rng(0).exponential(50, 200)

lo, hi = bootstrap_ci(data, np.mean)
print(f'95% CI: ({lo:.2f}, {hi:.2f})')

lo, hi = bootstrap_ci(data, np.median)
print(f'95% CI for median: ({lo:.2f}, {hi:.2f})')
```

### EM Algorithm

```python
from statkit.em import em_gmm
import numpy as np

rng = np.random.default_rng(42)
data = np.concatenate([rng.normal(0, 1, 300), rng.normal(5, 1, 300)])

result = em_gmm(data, n_components=2)
print(f'Estimated means: {sorted(result["mu"])}')
print(f'Mixing weights:  {result["pi"]}')
```

## Requirements

- Python 3.8+
- numpy >= 1.26.0
- scipy >= 1.11.0

## License

MIT
