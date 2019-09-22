# declaring the variables before hand
import numpy as np
import timeit


customType = np.dtype([('complexValue', np.complex)])
ndArrayData = np.array([[(0.5-2j), (2), (5.0-5j)], [(1), (0.5+2j), 7]], dtype=customType)  #

# yes there is a concept of rows and columns innermost list is seen as a row
# indexing is comman separated for n-dimensional indexing i.e. instead of `:`
# [a,b] means select `a` rows and `b` columns going from left to right
# with innermost comma separated row considered the origin
print("A:", ndArrayData, "\n\n")
print("selecting what is at index 0,1 : ", ndArrayData[0, 1], "\n\n")

# n-D slicing involves the creative use of 1-D slicing within [a, b]
allColumnsExceptLast = ndArrayData[:, :-1]  # select all rows/columns, not last 
print("All columns except last : ", allColumnsExceptLast, "\n\n")
lastColumn = ndArrayData[:, -1]  # selects all rows and only last column
print("Only last column : ", lastColumn, "\n\n")
