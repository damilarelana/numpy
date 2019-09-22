# declaring the variables before hand
import numpy as np
import timeit

# extract data from a clean file
x, y, z = np.loadtxt('./data/cleanColumnData.txt', skiprows=1, unpack=True)
print("x", x, "\n")
print("y", y, "\n")
print("z", z, "\n\n")

# extract data from a dirty file
a, b, c = np.genfromtxt('./data/dirtyColumnData.txt', dtype=float , unpack=True, filling_values=-0.9191, skip_header=1)
print("a", a, "\n")
print("b", b, "\n")
print("c", c, "\n\n")
      