# declaring the variables before hand
import numpy as np
import timeit


def randomWalkFast(n=1):
    steps = np.random.choice([-1, +1], n)  # gives random num in range -1 to +1
    return np.cumsum(steps)

print(timeit.timeit("randomWalkFast(100000)", number=1000, globals=globals()))