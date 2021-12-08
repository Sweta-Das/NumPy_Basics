# 0-D Array

import numpy as np
arr = np.array(42)  # elements in an array = 42 = 0-D
print(arr)

# 1-D Arrays

import numpy as np
ar = np.array([1, 2, 3, 4, 5])
print(ar)

# 2-D Arrays

import numpy as np
ab = np.array([[1, 2, 3], [4, 5, 6]])
print(ab)

# 3-D Arrays

import numpy as np
ac = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(ac)

# Checking Number of Dimensions - ndim attribute

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays

import numpy as np

ad = np.array([1, 2, 3, 4], ndmin = 5)
print(ad)
print('number of dimensions: ', ad.ndim)