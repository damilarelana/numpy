# declaring the variables before hand
import numpy as np
import timeit


customType = np.dtype([('complexValue', np.complex)])
ndArrayData = np.array([
      [(0.5-2j), (2), (5.0-5j), 112],
      [(1), 27, (0.5+2j), 7],
      [(3), (0.9+8j), 11, (11.5+9j)],
      [(5), (2.9+9j), 15, 45]], dtype=customType)

# define the split point `split`
split = 2

# splitting using the split point
leftData = ndArrayData[:split, :]  # all rows from beginning to split row 
rightData = ndArrayData[split:, :]  # al rows from split to the end
print("Left Data : ", leftData, "\n\n")
print("Right Data : ", rightData, "\n\n")