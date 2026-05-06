
import numpy as np

import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'


def SD_seasonal(T=300,seasonal_period=50,K=3,amplitude=1.0,random_phase=True,seed=None):

    rng = np.random.default_rng(seed)

    t = np.arange(T)
    s = np.zeros(T)

    for k in range(1, K + 1):
        a_k = rng.standard_normal() if random_phase else 1.0
        b_k = rng.standard_normal() if random_phase else 1.0

        s += (
            a_k * np.cos(2 * np.pi * k * t / seasonal_period) +
            b_k * np.sin(2 * np.pi * k * t / seasonal_period)
        )

    s = amplitude * s

    return s


