import os

import pandas as pd

from CreateData import create_single_time_series
from Remainder import SD_remainder
from Seasonal import SD_seasonal
from Trend import SD_trend

import matplotlib

from save import save_four_series

matplotlib.use('TkAgg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt



w = [0.3,0.3,0.4]                    # w is the weigth set of trend, seasonal and remainder. The sum of w must be 1
c = 4
c_scale = 5


T =300

random_trend_period = True
min_period = 30              # Only valid when random_trend_period = True
max_period = 100             # Only valid when random_trend_period = True
trend_period = 100           # Only valid when random_trend_period = False
#trend_type='linear'
trend_type='piecewise'
seed=None

seasonal_K=5
seasonal_period = 12
seasonal_amplitude=1.0


periodic=False
remainder_period = 50                  # Only valid when periodic=True
remainder_random_shape=False           # if True, alpha and beta is random
remainder_gamma_alpha=2.0,
remainder_gamma_beta=1.0,




# trend

trend = SD_trend(
    T=T,                                            # T : int, Time length
    random_trend_period=random_trend_period,        # random_trend_period : bool, Enable unfixed segment length
    min_period = min_period,                        # min_period : int, Minimum length of single section
    max_period = max_period,                        # max_period : int, Maximum length of single section
    trend_period=trend_period,                      # trend period : int, Period length
    trend_type=trend_type,                          # trend_type : str，
                                                    #      -linear : a single linear trend
                                                    #      -piecewise : segmented random trend, with each segment length being a period
    trend_slope=None,                               # trend_slope : float or None, linear trend slope, if None, randomly generated
    seed=seed                                       # seed : int or None
)


# seasonal

seasonal = SD_seasonal(
    T=T,                               # T : int, Time length
    seasonal_period=seasonal_period,   # seasonal_period : int, seasonal period length
    K=seasonal_K,                      # K : int, Harmonic quantity, K determines how many frequencies are added together to form a seasonal waveform
    amplitude=seasonal_amplitude,      # amplitude : float, enlarge or reduce the entire waveform as a whole
    seed=None                          # seed : int or None
)


# remainder

remainder = SD_remainder(
    T=T,                                    # T : int, Time length
    periodic=periodic,                      # periodic : bool, Whether to use periodic scale
    remainder_period=remainder_period,      # period : int, Period length (Only valid when periodic=True)
    shape=remainder_gamma_alpha,            # shape : float, Base shape parameter, alpha
    scale_base=remainder_gamma_beta,        # scale_base : float, Base scale, beta
    scale_amp=0.7,                          # scale_amp : float, Amplitude of scale variation (Only valid when periodic=True)
    random_shape=False,                     # random_shape : bool,  Whether to randomize shape per cycle
    zero_mean=True,                         # zero_mean : bool, Whether to center to zero mean
    seed=seed                               # seed : int or None
)



time_series = create_single_time_series(c,c_scale,w,trend,seasonal,remainder)

save_four_series(trend,seasonal,remainder,time_series,w,trend_type=trend_type)

# plt.figure(figsize=(12, 5))
# plt.plot(time_series, color='blue')
# plt.title('Original Time Series')
# plt.show()
#
#
# plt.figure(figsize=(12, 5))
# plt.plot(trend, color='red')
# plt.title('Trend Component')
# plt.show()
#
#
# plt.figure(figsize=(12, 5))
# plt.plot(seasonal, color='green')
# plt.title('Seasonal Component')
# plt.show()
#
#
# plt.figure(figsize=(12, 5))
# plt.plot(remainder, color='orange')
# plt.title('Remainder Component')
# plt.show()


fig, axes = plt.subplots(4, 1, figsize=(4, 4), sharex=True)

axes[0].plot(time_series, color='blue')
axes[0].set_title('Time Series')

axes[1].plot(trend, color='red')
axes[1].set_title('Trend')

axes[2].plot(seasonal, color='green')
axes[2].set_title('Seasonal')

axes[3].plot(remainder, color='orange')
axes[3].set_title('Remainder')

plt.tight_layout()
plt.show()
