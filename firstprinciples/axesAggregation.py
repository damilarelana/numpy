# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit
import matplotlib as plt

array = np.array([[1, 2, 3], [4, 5, 6]])


# summation along axis 0 i.e. across the rows in a column direction
caggregration = array.sum(axis=0)

# summation along axis 1 i.e. across the columns in a row direction
raggregration = array.sum(axis=1)

# print out the two times
print("Columnwise aggregration", caggregration, "\n")  # call/print
print("Rowwise aggregration", raggregration, "\n")  # call/print
