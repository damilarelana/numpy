# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit
import matplotlib.pyplot as plt


# define prices
prices = np.genfromtxt('./data/quasiRealisticData.txt', dtype=float , unpack=True, filling_values=10.9191)
print("Data:", prices, "\n")

# Plotting approach
min_price_index = np.argmin(prices)
max_price_index = min_price_index + np.argmax(prices[min_price_index:])
kwargs = {'markersize': 12, 'linestyle': ''} # define plot attributes

# generate plots
figure, axes = plt.subplots()
axes.plot(prices)
axes.set_title('Price History')
axes.set_xlabel('Time')
axes.set_ylabel('Price')
axes.plot(min_price_index, prices[min_price_index], color='green', **kwargs)
axes.plot(max_price_index, prices[max_price_index], color='red', **kwargs)
plt.show()
