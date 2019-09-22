import numpy as np
import timeit

# generate data
prices = np.full(1000, np.nan)  # fill with NaNs first
prices[[0, 25, 60, -1]] = [80.0, 30, 75, 50.0]
print("Data:", prices, "\n")


# linearly interpolate the missing values i.e. nan
x = np.arange(len(prices))  # autogenerate an array similar in size to prices [to rep x-axis of time for prices]
is_valid = ~np.isnan(prices)  # generate an array of True (of prices) based on `nan` locations
prices = np.interp(x=x, xp=x[is_valid], fp=prices[is_valid])  # autogenerate data points in coordinates of the NaN
prices += np.random.randn(len(prices)) * 7  # generate random data noise from binomial distribution
print("Data:", prices, "\n")

# save the data
np.savetxt('./data/quasiRealisticData.txt', prices, delimiter=',')
