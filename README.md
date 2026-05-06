# PanelTS-Panel-Based-Benchmark-Dataset

---
license: cc-by-4.0
pretty_name: PanelTS
tags:
- time-series
- forecasting
- panel-data
- benchmark
- tabular
- timeseries
- synthetic-data
- mlcroissant
- pandas
task_categories:
- time-series-forecasting
---

# PanelTS: A Panel-based Time Series Forecasting Dataset

## Dataset Description

PanelTS is a panel-based time series forecasting dataset designed for evaluating forecasting models on multiple related units observed over time. Each unit has its own target variable and associated covariates, while unit identities are explicitly preserved.

The dataset is designed to support univariate, multivariate, and panel-based forecasting tasks under a unified data format.

## Dataset Domains

PanelTS includes multiple domains:

- Synthetic panel time series with controllable temporal patterns
- COVID-19 dynamics
- Exchange-traded funds
- Currency exchange rates
- Stock market time series


## Dataset Splits

The dataset provides standardized train, validation, and test splits for evaluating forecasting models under different settings.

The splits are designed to support comparisons across:

- Different input lengths
- Different prediction horizons
- Different temporal granularities
- Different panel structures

## Intended Use

PanelTS is intended for academic research on:

- Panel-based time series forecasting
- Multi-unit forecasting
- Multi-system prediction
- Forecasting benchmark evaluation
- Cross-unit temporal dependency modeling
- Synthetic pattern analysis

The dataset can be used to evaluate both traditional forecasting models and deep learning-based time series models.

## Out-of-Scope Use

This dataset is not intended for direct use in high-stakes decision-making, including:

- Medical diagnosis
- Public health policy decisions
- Financial investment decisions
- Trading strategies
- Credit or insurance decisions
- Any automated decision system affecting individuals

Models trained or evaluated on this dataset should be further validated before being used in real-world applications.


## Potential Biases

Potential biases include:

- Selection bias in the choice of domains, units, and time periods
- Reporting bias in public health data
- Survivorship and availability bias in financial market data
- Design bias in synthetic data generation
- Differences in temporal coverage and data quality across domains

These biases may affect model performance comparisons and generalization to unseen domains.

## Personal and Sensitive Information

The dataset does not contain individual-level personal information.

The real-world subsets are based on aggregated public time series or market-level data. No personally identifiable information, demographic attributes, private health records, or individual-level sensitive information is included.

## Synthetic Data

PanelTS includes synthetic panel time series generated to evaluate controlled temporal patterns and panel structures. The generation process and parameters are described in the accompanying documentation.

## License

This dataset is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0), unless otherwise stated for specific source-derived subsets.
