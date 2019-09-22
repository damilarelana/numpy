# Numpy Broadcasting
import numpy as np
import timeit

# Equal dimensions
a = np.ones((3, 4), dtype=float)
print("initial A (", a.shape, ")\n", a, "\n\n")

b = np.random.random((3, 4))  # generate 3*4 randum numbers arranged 3 by 4
print("initial B (", b.shape, ")\n", b, "\n\n")

# summation
print("A + B (", (a+b).shape, ")\n", a + b, "\n\n")

# Unequal dimensions BUT one dimension is equal to 1
c = np.ones((3, 4), dtype=float)
print("initial C (", c.shape, ")\n", c, "\n\n")

d = np.arange(4)
print("initial D (", d.shape, ")\n", d, "\n\n")

# summation
print("C + D  (", (c+d).shape, ")\n", c + d, "\n\n")

# Unequal dimensions BUT compatible in all dimensions
e = np.ones((3, 4), dtype=float)
print("initial E (", e.shape, ")\n", e, "\n\n")

f = np.random.random((5, 1, 4))
print("initial F (", f.shape, ")\n", f, "\n\n")

# summation
print("E + F  (", (e+f).shape, ")\n", e + f, "\n\n")
