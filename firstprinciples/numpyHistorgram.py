# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit
import matplotlib.pyplot as plt


# define the data
array_data = np.array([[[1,2,3,4], [5,6,7,8]], [[1,2,3,4], [9,10,11,12]]], dtype=np.int64)


# construct the histogram
plt.hist(array_data.ravel(), bins=range(0, 13))

# construct the image
plt.title("Frequency of 3D Array Elements")
plt.show()
