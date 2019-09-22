# declaring the variables before hand
import numpy as np
import timeit


ndArrayData = np.array([2, 2, 1, 5], dtype=float)  # simple ndarray

# negative index counts from the back, using the array lenght as the back 
# [-1] means the last element i.e. [len(a)-1]
print("Last element is: ", ndArrayData[-1], "\n\n")
print("All elements in normal order: ", ndArrayData[:])

# `[a:b:c]` means count in increments of `c` starting at `a` inclusive to `b-1`
# assuming `c` is positive. 
# if c is negative you count backwards, if omitted it is 1. 
# if `a` omitted then start at extreme in direction you're counting from
# i.e. `a` if c > 0 
# i.e. `b` if c < 0
# if `b` omitted then end as far as possible in direction you're counting to
# meaning that when c < 0
#   a becomes the end point such that the first `:` is now interpreted as end
#   b becomes the start points such that the second `:` is interpreted as start
# thus [`::-1`] means count backwards from extreme right to extreme left
print("All elements in reversed order: ", ndArrayData[::-1])