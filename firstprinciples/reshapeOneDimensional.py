# declaring the variables before hand
import numpy as np
import timeit

a = np.arange(24)  # create 1-D ndarray with 24 element
b = a.reshape(2, 4, 3)
c = b.shape
print("A is ", a, "\n\n", "A's dimension is ", a.ndim, "\n\n", "B is ", b, "\n\n", "B's shape is ", c, "\n\n",  "B's attributes are ", b.flags)