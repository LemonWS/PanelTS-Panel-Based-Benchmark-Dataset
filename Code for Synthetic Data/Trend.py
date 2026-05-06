
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'

import matplotlib.pyplot as plt


def SD_trend(T=300, random_trend_period=False, trend_period=50,
             trend_type='linear', trend_slope=None,
             intercept=None, intercept_scale=50.0,
             min_period=20, max_period=50, seed=None):



    rng = np.random.default_rng(seed)
    t = np.arange(T)
    trend = np.zeros(T)


    if intercept is None:
        intercept = rng.normal(0, intercept_scale)


    if trend_type == 'linear':
        slope = rng.uniform(-1, 1) if trend_slope is None else trend_slope
        trend = intercept + slope * t


    elif trend_type == 'piecewise':

        if random_trend_period:
            segments = [0]
            while segments[-1] < T:
                seg_len = rng.integers(min_period, max_period + 1)
                segments.append(segments[-1] + seg_len)
            segments = np.array(segments)
        else:
            segments = np.arange(0, T + trend_period, trend_period)

        current_value = intercept

        for i in range(len(segments) - 1):
            start = segments[i]
            end = min(segments[i + 1], T)
            seg_length = end - start

            slope = rng.uniform(-1, 1) if trend_slope is None else trend_slope
            local_trend = current_value + slope * np.arange(seg_length)

            trend[start:end] = local_trend
            current_value = local_trend[-1]

    else:
        raise ValueError("trend_type must be 'linear' or 'piecewise'")

    return trend




# T = 300
# period = 50
# linear = SD_trend(T, trend_type='linear', seed=None)
# piecewise = SD_trend(T, period=period, trend_type='random_piecewise', seed=None)
#
# plt.figure(figsize=(12, 5))
# plt.plot(linear, label='Linear Trend')
# plt.plot(piecewise, label='Random Piecewise Trend')
# plt.legend()
# plt.show()


# def SD_trend(T=300, period=50, trend_type='piecewise', slope=None, seed=None):
#     rng = np.random.default_rng(seed)
#     t = np.arange(T)
#     trend = np.zeros(T)
#
#     if trend_type == 'linear':
#         if slope is None:
#             slope = rng.uniform(-1, 1)
#         trend = slope * t
#
#     elif trend_type == 'piecewise':
#         segments = np.arange(0, T, period)
#         current_value = 0
#         for i in range(len(segments)):
#             start = segments[i]
#             end = segments[i + 1] if i + 1 < len(segments) else T
#             seg_length = end - start
#             seg_slope = rng.uniform(-1, 1) if slope is None else slope
#             trend[start:end] = current_value + seg_slope * np.arange(seg_length)
#             current_value = trend[end - 1]
#
#     else:
#         raise ValueError("trend_type must be 'linear' or 'piecewise'")
#
#     return trend

# trend = SD_trend(T=300, period=50, trend_type='piecewise', slope=None)
# import matplotlib.pyplot as plt
# plt.plot(trend)
# plt.show()