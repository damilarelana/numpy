# these functions seek to check whether or not a given list of arrays are broadcastable
# i.e. whethe their shape is such that they follow the 3 broadcast rules
# - exactly same shape
# - common dimension or a 1 when different
# - mialigned array can be prepended with a dimension of length 1


# Pure Python
import numpy as np
import timeit
import matplotlib as plt


# define the set of arrays to be tested
a = np.sin(np.arange(10)[:, None])
b = np.random.randn(1, 10)
c = np.full_like(a, 10)
d = 8

input_array_tuple = (a, b, c, d)

# define the bespoke broadcastability checker function
def can_broadcast(*arrays) -> bool:
    arrays = [np.atleast_1d(array) for array in arrays]  # list comprehension to generate an array

    # test rule 1 to see if they the arrays are exactly the same shape
    if len(set(array.shape for array in arrays)) == 1:
        return True

    # test rule 2 to see if dimenions are same, and if dimension length are common (or 1)
    if len(set((array.ndim) for array in arrays)) == 1:
        return True

    # test rule 3 to adjust the array with mismatched shaped by prepending a dimension of length 1
    arrays_maxdimension = max(array.ndim for array in arrays)    # determine what the largest dimension is

    # use the maximum dimension to test and reshape, to generate an array of shapes
    array_shapes = np.array([(1,) * (arrays_maxdimension - array.ndmin) + array.shape for array in arrays]) 

    # mask sections in the array_shapes, where we have a `1` i.e. penultimate step to complete test of rule 3 
    masked_array = np.ma.masked_where(array_shapes == 1, array_shapes)  

    # test remaining sections to ensure the dimension length are `common` i.e. the same which means the ptp() would be zero as max=min
    return np.all(masked_array.ptp(axis=0) == 0)  # this only returns `True` if the other remaining dimensions have a common length


# define the numpy library based broadcastability checker
def can_broadcast_numpy(*arrays) -> bool:
    try:
        np.broadcast(*arrays)  # this returns a broadcast object
        return True
    except ValueError:
        return False


# compare to check if the two functions gave the same answer
if np.allclose(can_broadcast_numpy(input_array_tuple), can_broadcast(input_array_tuple)):
    print("can_broadcast_numpy() is equivalent to can_broadcast() \n")
