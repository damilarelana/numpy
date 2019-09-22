# declaring the variables before hand
import numpy as np
import timeit

a = np.ones(24)  # create 1-D ndarray with 24 element
b = np.zeros([2, 4, 3], dtype=int)
c = np.empty((10, 1), dtype='a')
d = np.zeros((2, 2), dtype=[('c', 'f')])  # a custom type [('name', 'dtype')]
customType = np.dtype([('complexValue', np.complex)])
e = np.array([[(2), (2)], [(1), (1)]], dtype=customType)  # a custom type
print("A:", a, "\n", "B:", b, "\n", "C:", c, "\n", "D:", d, "\n", "E:", e)
print(type(e))
print(b.dtype.name)
print(e.dtype.name)