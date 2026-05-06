import numpy as np

from Remainder import SD_remainder
from Seasonal import SD_seasonal
from Trend import SD_trend


def create_single_time_series(c,c_scale, w, trend, seasonal, remainder,seed=None):   # w is the weigth set of trend, seasonal and remainder
                                                                   # c is the intercept
    rng = np.random.default_rng(seed)
    if c is None:
        c = rng.normal(0, c_scale)

    time_series = c + w[0] * trend + w[1] * seasonal + w[2] * remainder

    return time_series




# def create_single_time_series(c, g, s, r, l):   #x,y,z are the weigth of trend, seasonal and remainder
#     time_series = []                            #l is the length of time series
#                                                 #c is the intercept
#     if g+s+r == 1:
#         for i in range(l):
#
#             y = c + g * SD_trend(i) + s * SD_seasonal(i) + r * SD_remainder(i)
#             time_series.append(y)
#
#         return time_series
#
#     else:
#         print("g + s + r must be 1")