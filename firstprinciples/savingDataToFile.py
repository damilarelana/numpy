import numpy as np
import timeit

# generate data
data_to_save = np.arange(0.0, 0.5, 0.01)
print("Data:", data_to_save, "\n")


# save the data
np.savetxt('./data/savedData.txt', data_to_save, delimiter=',')
