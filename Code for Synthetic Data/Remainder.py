import numpy as np


def SD_remainder(T=300,periodic=False,remainder_period=50,shape=2.0,scale_base=1.0,scale_amp=0.5,random_shape=False,zero_mean=True,seed=None):

    # T : int, Time length
    # periodic : bool, Whether to use periodic scale
    # remainder_period : int, Period length (Only valid when periodic=True)
    # shape : float, Base shape parameter
    # scale_base : float, Base scale
    # scale_amp : float, Amplitude of scale variation (Only valid when periodic=True)
    # random_shape : bool,  Whether to randomize shape per cycle
    # zero_mean : bool, Whether to center to zero mean
    # seed : int or None,


    rng = np.random.default_rng(seed)
    t = np.arange(T)

    if periodic:
        scale_t = scale_base * (1 + scale_amp * np.sin(2 * np.pi * t / remainder_period))
    else:
        scale_t = np.full(T, scale_base)


    scale_t = np.clip(scale_t, 1e-3, None)

    r = np.zeros(T)

    for i in range(T):
        alpha = shape
        if random_shape:
            alpha = rng.uniform(1.5, 3.0)

        r[i] = rng.gamma(shape=alpha, scale=scale_t[i])

    if zero_mean:
        r = r - r.mean()

    return r
