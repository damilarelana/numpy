# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit
import matplotlib as plt


# define prices
prices = np.genfromtxt('./data/quasiRealisticData.txt', dtype=float , unpack=True, filling_values=10.9191)
print("Data:", prices, "\n")


def calc_profit(price_array) -> int:
    max_profit = 0  # initialize the maximum profit i.e. assuming you sell at cost price
    cost_price = price_array[0]  # initialize the initial cost price
    sales_price = price_array[0]  # initialize the current sale price
    for price in price_array[1:]:  # iterate over price array while skipping price_array[0]
        cost_price = min(price, cost_price)  # compare/swap to find ideal cost price
        sales_price = max(sales_price, price)  # compare/swap to find ideal sale price
        max_profit = max(sales_price - cost_price, max_profit)  # get new profit at current cost/sales prices
    return max_profit  # returns the computed maximum profit


def calc_profit_numpy(price_array) -> int:
    cummin = np.minimum.accumulate
    prices = np.asarray(price_array)
    return np.max(prices - cummin(prices))


# calculate time to run `n` executions
n = 25000
calc_profit_timing_purepython = timeit.timeit("calc_profit(prices)", number=n, globals=globals())
calc_profit_timing_numpy = timeit.timeit("calc_profit_numpy(prices)", number=n, globals=globals())


# compare to check if the two functions gave the same answer
if np.allclose(calc_profit(prices), calc_profit_numpy(prices)):
    print("Calc_Profit() is equivalent to Calc_Profit_Numpy() \n")

# print out the two times
print("Profit calculatin (purePython)", calc_profit_timing_purepython, "secs \n")  # call/print
print("Profit calculatin (numpy)", calc_profit_timing_numpy, "secs \n")  # call/print


# compare the two times
print("Timing difference: {:0.1f}x".format(calc_profit_timing_purepython / calc_profit_timing_numpy))
