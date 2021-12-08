import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])   # getting 1st array element

print(arr[2] + arr[3])

#######################################################
# Accessing 2D Arrays

import numpy as np

ab = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print('2nd element on 1st dimension: ', ab[0, 1])

print('3rd element of 2nd dimension: ', ab[1, 2])

#######################################################
# Accessing 3D Arrays

import numpy as np

ac = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(ac[0, 1, 2])   # dim: 1st, 2nd, 3rd

########################################################
# Negative Indexing

ad = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', ad[1, -1])

print('Last element from 1st dim: ', ad[0, -1])