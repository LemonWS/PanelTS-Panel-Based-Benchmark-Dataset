import pandas as pd
import numpy as np

from Remainder import SD_remainder
from Seasonal import SD_seasonal
from Trend import SD_trend


def generate_panel_data_independent(N=5, T=100, nx=3, random_trend_period=False, trend_period=50,
                                    trend_type='linear', trend_slope=None, seasonal_period=12, K=3, periodic=False,
                                    seed=None):
    rng = np.random.default_rng(seed)

    def generate_season(T, period, K=3):
        t = np.arange(T)
        season = np.zeros(T)
        for k in range(1, K + 1):
            amp = rng.uniform(0.5, 1.5)
            phase = rng.uniform(0, 2 * np.pi)
            season += amp * np.sin(2 * np.pi * k * t / period + phase)
        return season

    data_list = []

    for i in range(N):
        t = np.arange(T)
        X = np.zeros((T, nx))

        for j in range(nx):
            trend_x = SD_trend(T, random_trend_period, trend_period, trend_type, trend_slope, seed)
            season_x = SD_seasonal(T, seasonal_period, K, amplitude=1.0)
            remainder_x = SD_remainder(T, periodic)
            X[:, j] = trend_x + season_x + remainder_x

        trend_y = SD_trend(T, random_trend_period, trend_period, trend_type, trend_slope, seed)
        season_y = SD_seasonal(T, seasonal_period, K, amplitude=1.0)
        remainder_y = SD_remainder(T, periodic)

        # 随机回归系数
        beta = rng.uniform(-2, 2, size=nx)
        y = trend_y + season_y + X @ beta + remainder_y

        df = pd.DataFrame(X, columns=[f'x{j + 1}' for j in range(nx)])
        df['y'] = y
        df['id'] = i
        df['time'] = t
        data_list.append(df)

    panel_df = pd.concat(data_list, ignore_index=True)
    return panel_df

# def generate_panel_data_with_coeff(
#         N=5, T=10, seed=None,
#         include_alpha=True, alpha_std=1.0,
#         include_time_trend=True, beta_time=0.5,
#         include_random_slope=False, slope_std=0.1,
#         include_seasonality=False, season_period=4, season_amp=1.0,
#         include_X=False, X_dim=2, X_coeff=None, X_std=1.0,
#         noise_std=1.0
# ):
#
#     rng = np.random.default_rng(seed)
#
#     individuals = np.arange(1, N + 1)
#     time = np.arange(1, T + 1)
#
#     panel = pd.DataFrame([(i, t) for i in individuals for t in time],
#                          columns=['id', 'time'])
#
#
#     if include_alpha:
#         alpha = rng.normal(0, alpha_std, size=N)
#         panel['alpha'] = panel['id'].map(dict(zip(individuals, alpha)))
#     else:
#         panel['alpha'] = 0.0
#
#
#     if include_time_trend:
#         panel['time_trend'] = beta_time * panel['time']
#     else:
#         panel['time_trend'] = 0.0
#
#
#     if include_random_slope:
#         slope_i = rng.normal(0, slope_std, size=N)
#         panel['random_slope'] = panel['id'].map(dict(zip(individuals, slope_i))) * panel['time']
#     else:
#         panel['random_slope'] = 0.0
#
#
#     if include_seasonality:
#         panel['season'] = season_amp * np.sin(2 * np.pi * panel['time'] / season_period)
#     else:
#         panel['season'] = 0.0
#
#
#     if include_X:
#         X_coeff = X_coeff or np.ones(X_dim)
#         for j in range(X_dim):
#             panel[f'X{j + 1}'] = rng.normal(0, X_std, size=N * T)
#     else:
#         X_dim = 0
#
#
#     panel['epsilon'] = rng.normal(0, noise_std, size=N * T)
#
#
#     y = panel['alpha'] + panel['time_trend'] + panel['random_slope'] + panel['season'] + panel['epsilon']
#
#     if include_X:
#         for j in range(X_dim):
#             y += X_coeff[j] * panel[f'X{j + 1}']
#
#     panel['y'] = y
#
#     return panel
#
#
#
# df = generate_panel_data_with_coeff(
#     N=5, T=12,
#     include_random_slope=True,
#     include_seasonality=True,
#     include_X=True, X_dim=3, X_coeff=[2.0, -1.5, 0.5],
#     seed=42
# )
# print(df.head(12))


#
#
# def generate_panel_data(N=10, T=100, p=3,
#                         trend_type='linear', season_period=12,
#                         noise_std=1.0, seed=None):
#
#     rng = np.random.default_rng(seed)
#
#     def generate_trend(t, slope=None):
#         if trend_type == 'linear':
#             if slope is None:
#                 slope = rng.uniform(-0.5, 0.5)
#             return slope * t
#         elif trend_type == 'random_piecewise':
#
#             segments = [0, T // 2, T]
#             trend = np.zeros_like(t, dtype=float)
#             for i in range(len(segments) - 1):
#                 s = rng.uniform(-0.5, 0.5)
#                 trend[segments[i]:segments[i + 1]] = s * np.arange(segments[i + 1] - segments[i])
#             return trend
#         else:
#             return np.zeros_like(t)
#
#     def generate_season(T, period, K=3):
#         t = np.arange(T)
#         season = np.zeros(T)
#         for k in range(1, K + 1):
#             amp = rng.uniform(0.5, 1.5)
#             phase = rng.uniform(0, 2 * np.pi)
#             season += amp * np.sin(2 * np.pi * k * t / period + phase)
#         return season
#
#     data_list = []
#
#
#     for i in range(N):
#         t = np.arange(T)
#         X = np.zeros((T, p))
#
#
#         for j in range(p):
#             trend = generate_trend(t)
#             season = generate_season(T, season_period)
#             remainder = rng.normal(0, noise_std, T)
#             X[:, j] = trend + season + remainder
#
#
#         beta = rng.uniform(-2, 2, size=p)
#         trend_y = generate_trend(t)
#         season_y = generate_season(T, season_period)
#         remainder_y = rng.normal(0, noise_std, T)
#         y = trend_y + season_y + X @ beta + remainder_y
#
#
#         df = pd.DataFrame(X, columns=[f'x{j + 1}' for j in range(p)])
#         df['y'] = y
#         df['id'] = i
#         df['time'] = t
#         data_list.append(df)
#
#     panel_df = pd.concat(data_list, ignore_index=True)
#     return panel_df
#
#
#
# panel_data = generate_panel_data(N=10, T=50, p=10, seed=42)
# print(panel_data.head(10))
