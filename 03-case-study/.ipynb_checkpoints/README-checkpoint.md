# 03 — Economic Data Analysis

Exploratory analysis of four key US macroeconomic indicators sourced directly from the FRED (Federal Reserve Economic Data) database, covering 1990 to present.

---

## Overview

| Indicator | FRED Code | Frequency | Description |
|-----------|-----------|-----------|-------------|
| GDP | `GDP` | Quarterly | US Gross Domestic Product (billions USD) |
| CPI | `CPIAUCSL` | Monthly → Quarterly | Consumer Price Index (1982-84 = 100) |
| Unemployment Rate | `UNRATE` | Monthly → Quarterly | US civilian unemployment rate |
| Federal Funds Rate | `FEDFUNDS` | Monthly → Quarterly | Federal Reserve benchmark interest rate |

145 quarterly observations from 1990 Q1 to present.

---

## Key Findings

- GDP has grown from $5.9 trillion in 1990 to over $30 trillion today, with brief contractions in 2008–09 and 2020
- The 2021–2022 inflation surge (peaking above 8%) represents the sharpest price acceleration since the 1980s
- The classical Phillips Curve relationship breaks down in the post-pandemic period — low unemployment and high inflation coexisted, driven by supply-side shocks
- The Fed Funds Rate shows a persistent lag behind inflation, with the 2022–2023 hiking cycle being the most aggressive in 40 years

---

## Visualizations

**1. Time Series Overview** — Long-run trends and cyclical behavior of all four indicators, with NBER recession periods shaded

![Time Series](./macro_timeseries.png)

**2. Correlation Matrix** — Pairwise correlations across the four indicators

![Correlation Matrix](./macro_correlation.png)

**3. Phillips Curve** — Inflation vs. unemployment across time, colored by year

![Phillips Curve](./phillips_curve.png)

**4. Fed Funds Rate vs. Inflation** — Monetary policy response to inflation across three decades

![Fed Funds vs Inflation](./fedfunds_vs_inflation.png)

---

## Requirements

```bash
pip install numpy pandas matplotlib fredapi
