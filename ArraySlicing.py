import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:5])   # slices elements from I.N. = 1 to I.N. = 4

print(arr[4:])
print(arr[:4])

#######################################################
# Negative Slicing

print(arr[-3:-1])

######################################################
# Step

print(arr[1:5:2])   # returns every other element from index 1 to 5
print(arr[::2])   # returns every other element from the entire array

#####################################################
# Slicing 2-D Arrays

import numpy as np
aa = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(aa[1, 1:4])   # from 2nd element, slice elements from index 1 to 4 (not included)

print(aa[0:2, 2])   # from both elements, return index 2

print(aa[0:2, 1:4])   # from both elements, slice index 1 to 4 (not included); returns 2D
