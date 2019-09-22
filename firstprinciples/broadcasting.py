# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit
import matplotlib as plt


# generate random numbers from the Gaussian distribution i.e. binomial distribution [helps to generate around a known mean and variance]
array = np.random.normal(loc=[2, 20], scale=[1., 3.5], size=(3, 2))


# mean along axis 0 i.e. across the rows in a column direction
cmean = array.mean(axis=0)

# min along axis 1 i.e. across the columns in a row direction
cmin = array.min(axis=1)  # [:,None] is used to stretch incompatible shape suitable for broadcasting 
print("Cmin (without expansion): \n", cmin, "\n")
print("Cmin (with expansion): \n", cmin[:, None], "\n")



# use broadcast to subtract column-wise mean array from the original array i.e. shape (1, 2) from shape (3,2)
# column dimension are equal
# hence the broadcasting would occur along the row axis is axis=0
# note that (1,2) is represented as (2,) within numpy

# determine substraction and print
subtrtnmean = array - cmean
subtrtnmin = array - cmin[:, None]


# determine z-score
zscoreavalue = subtrtnmean/array.std(axis=0)


# print out the results
print("Original array\n", array, "\n")
print("Columnwise mean\n", cmean, "\n")
print("Rowwise min\n", cmin, "\n")
print("broadcasted substraction (array - cmean): \n", subtrtnmean, "\n")
print("broadcasted substraction (array - cmin): \n", subtrtnmin, "\n")
print("Z-Score columnwise: \n", zscoreavalue, "\n")
