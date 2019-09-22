# declaring the variables before hand
import numpy as np
import timeit

a = np.arange(10000)  # create 1-D ndarray with 10000 element
b = a.reshape(100, 100)
c = b > 9900  # this returns an nd
d = b.dot(b)  # this performs the normal matrix multiplications
e = d * d  # this is an element wise multiplication
f = np.logspace(10, 25, 5)  # logarithmic space e..g 10^25. 5 is how many
g = np.linspace(10, 25, 5)  # linear space with 5 being number of elements
print("B is ", b, "\n\n", "C is ", "\n\n", c, "D is ", "\n\n", d, "E is ", 
      "\n\n", e, "F is ", "\n\n", f, "G is ", "\n\n", g)