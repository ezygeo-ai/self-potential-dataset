# Code was created by M. Heriyanto, 2019/10/28
# Ref: H.M. El-Kaliouby & M.A. Al-Garni. J. Geophys. Eng. 6 (2009) 29-34.

import numpy as np
import random as rd
import pickle


# SP forward function
def SPfunc(x, par):
    h = par[0]
    a = par[1]
    alpha = par[2]
    k = par[3]
    x0 = par[4]
    SPdata = []
    for i in x:
        var_up = ((i - x0) - a * np.cos(alpha)) ** 2 + (h - a * np.sin(alpha)) ** 2
        var_down = ((i - x0) + a * np.cos(alpha)) ** 2 + (h + a * np.sin(alpha)) ** 2
        var = k * np.log(var_up / var_down)
        SPdata.append(var)

    # give noise for data (Gaussian distribution)
    target_snr_db = 25  # set a target SNR
    x_watts = list(map(lambda xin: pow(xin, 2), SPdata))
    sig_avg_watts = np.mean(x_watts)
    sig_avg_db = 10 * np.log10(sig_avg_watts)
    noise_avg_db = sig_avg_db - target_snr_db
    noise_avg_watts = 10 ** (noise_avg_db / 10)
    mean_noise = 0
    noise_data = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(SPdata))
    SPdata_noise = SPdata + noise_data

    return SPdata_noise


# === MAKE SYNTHETIC DATASET
min_ht = 5
max_ht = 15
n_ht = 5    # point
val_h = np.linspace(min_ht, max_ht, n_ht)

min_a = 2
max_a = 8
n_a = 5     # point
val_a = np.linspace(min_a, max_a, n_a)

min_alpha = 20
max_alpha = 60
n_alpha = 7     # point
val_alpha = np.linspace(min_alpha, max_alpha, n_alpha)

min_k = 70
max_k = 130
n_k = 7     # point
val_k = np.linspace(min_k, max_k, n_k)

min_x0 = -15
max_x0 = 30
n_x0 = 7    # point
val_x0 = np.linspace(min_x0, max_x0, n_x0)

dataset = []
ndata = 6125
for it_dat in range(ndata):
    # hs = min_ht + (max_ht - min_ht) * np.random.rand()
    hs = rd.choice(val_h)

    # a_s = min_a + (max_a - min_a) * np.random.rand()
    a_s = rd.choice(val_a)

    # alphas = min_alpha + (max_alpha - min_alpha) * np.random.rand()
    alphas = rd.choice(val_alpha)

    # ks = min_k + (max_k - min_k) * np.random.rand()
    ks = rd.choice(val_k)

    # x0s = min_x0 + (max_x0 - min_x0) * np.random.rand()
    x0s = rd.choice(val_x0)

    par_mod = [hs, a_s, alphas, ks, x0s]

    measure_loc = np.arange(-80, 80, 2)  # Location of measurement
    get_SPData = SPfunc(measure_loc, par_mod)
    dataset.append((par_mod, get_SPData))  # [(input, output)]


with open('SP_Dataset.pickle', 'wb') as f:
    pickle.dump(dataset, f)
