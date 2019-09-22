# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit


# define prices
prices = np.array([20, 18, 14, 17, 20, 21, 15])


def calc_profit(price_array) -> (int, int, int):
    max_profit = 0  # initialize the maximum profit i.e. assuming you sell at cost price
    cost_price = price_array[0]  # initialize the initial cost price
    sales_price = price_array[0]  # initialize the current sale price
    for price in price_array[1:]:  # iterate over price array while skipping price_array[0]
        cost_price = min(price, cost_price)  # compare/swap to find ideal cost price
        sales_price = max(sales_price, price)  # compare/swap to find ideal sale price
        max_profit = max(sales_price - cost_price, max_profit)  # get new profit at current cost/sales prices
    return (cost_price, sales_price, max_profit)


# calculate time to run `n` executions
n = 1
calc_profit_timing = timeit.timeit("calc_profit(prices)", number=n, globals=globals())

# print out the two times
print("calc_profit code took about", calc_profit_timing, "secs \n")  # call/print

# display the identified values
(cost_price, sales_price, max_profit) = calc_profit(prices)
print("Ideal Cost Price is:", cost_price, "\n")
print("Ideal Sales Price is:", sales_price, "\n")
print("Giving a maximum profit of:", max_profit, "\n")
