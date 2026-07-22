# Stats Playground

A structured collection of statistical algorithm implementations, visualizations, and real-world data analysis projects — built from scratch in Python and R.

---

## Structure

| Phase | Topic | Description |
|-------|-------|-------------|
| [01 — Algorithms](./01-algorithms/) | Algorithm Implementations | Monte Carlo, Bootstrap, EM Algorithm |
| [02 — Visualizations](./02-visualizations/) | Statistical Visualizations | CLT, Bayesian Updating, Hypothesis Testing |
| [03 — Case Study](./03-case-study/) | Economic Data Analysis | US macroeconomic indicators from FRED (1990–present) |

---

## 01 — Algorithm Implementations

From-scratch implementations of three classical statistical algorithms, each with step-by-step code, visualizations, and analysis.

- **Monte Carlo** — Estimate π via random sampling; convergence and error decay analysis
- **Bootstrap** — Confidence intervals via resampling without distributional assumptions
- **EM Algorithm** — Gaussian Mixture Model parameter estimation via Expectation-Maximization

→ [View folder](./01-algorithms/)

---

## 02 — Statistical Visualizations

Interactive and static visualizations of foundational statistical concepts.

- **Central Limit Theorem** — Convergence to normality across sample sizes and population shapes
- **Bayesian Updating** — Sequential posterior updating with Beta-Binomial conjugacy
- **Hypothesis Testing** — p-values, rejection regions, Type I/II errors, and statistical power

→ [View folder](./02-visualizations/)

---

## 03 — Economic Data Analysis

Exploratory analysis of four US macroeconomic indicators (GDP, CPI, Unemployment Rate, Fed Funds Rate) sourced from FRED, covering 1990 to present.

- Time series overview with recession shading
- Correlation matrix across indicators
- Phillips Curve: inflation vs. unemployment
- Fed Funds Rate vs. inflation: monetary policy response

→ [View folder](./03-case-study/)

---

## Requirements

```bash
pip install numpy pandas matplotlib scipy fredapi
