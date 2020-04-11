# declaring the variables before hand
import numpy as np
import timeit

a = np.empty((2, 3))
print("Empty multi-dimensional array A is:\n {}\n".format(a))

a = np.ones((2, 3), dtype=float)
print("initial A", "\n", a, "\n\n")

b = np.random.choice([-1, +1], 6)  # this generates a list of 6 random numbers
print("initial B", "\n", b, "\n\n")

a *= 15  # element multiplication by 15
print("post A", "\n", a, "\n\n")
a += b.reshape(a.shape)  # extract the dimensions of a and use to reshape b
print("casting B to A", "\n", a, "\n\n")

f = np.exp(a*1j)  # exp() means e^x 
print("F ", "\n", f, "\n\n")

print("Maximum element value of A is ", "\n", a.max(), "\n\n",
      "Minimum element value of A is ", "\n", a.min(), "\n\n",
      "Sum of element values of A is ", "\n", a.sum())
