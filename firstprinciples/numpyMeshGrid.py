# Given a stock’s price history as a sequence, and
# assuming that you are only allowed to make one purchase and one sale, 
# what is the maximum profit that can be obtained?
# For example, given prices = (20, 18, 14, 17, 20, 21, 15), 
# the max profit would be 7, from buying at 14 and selling at 21.

# Pure Python
import numpy as np
import timeit
import matplotlib.pyplot as plt


# define the data
array_data = np.arange(-5, 5, 0.01)


# generate mesh grid
x_data, y_data = np.meshgrid(array_data, array_data)
z_data = np.sqrt(x_data**2 + y_data**2) 


# generate the image on the mesh grid axes
plt.imshow(z_data, cmap=plt.cm.gray)


# draw a color bar
plt.colorbar()

# show the plot
plt.show()
