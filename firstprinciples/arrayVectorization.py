# Numpy Vectorization
import numpy as np
import timeit


# seed the random number generator
np.random.seed(444)


# generate random 1-D array of true or false elements
a = np.random.choice([False, True], size=100000)
print("initial A:", a, "\n")


# compare and count transitions from `False` to `True`
# extract array slice from 1st element uptill the second to last element
# extract another array from 2nd element uptill the last element
# create another array of tuples [element_n, element_n+1] using zip()
def transition_count_forloop(array) -> int:
    counter = 0
    for i, j in zip(array[:-1], array[1:]):  # extract transition tuple to test
        if not j and i:  # if `i is False` and `j is True`
            counter += 1  # increment the counter, as there is a transition
    # print(counter, "ForLoop transitions \n")
    return counter


# vectorized form, without using for loop
def transition_count_vectorized(array) -> int:
    counter = np.count_nonzero(a[:-1] < a[1:])
    # print(counter, "Vectorized transitions \n")
    return counter  # check/count transition


# time 1000 executions
forloop_timing = timeit.timeit("transition_count_forloop(a)", number=1000, globals=globals())
vectorized_timing = timeit.timeit("transition_count_vectorized(a)", number=1000, globals=globals())


# print out the two times
print("ForLoop transitions took", forloop_timing, "secs \n")  # call/print
print("Vectorized transitions took", vectorized_timing, "secs \n")  # call/print


# compare the two times
print("Timing difference: {:0.1f}x".format(forloop_timing / vectorized_timing))
