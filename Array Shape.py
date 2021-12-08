import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # 2-D array
print(arr.shape)


# Create an array with 5 dimensions using "ndmin" using a vector with values 1,2,3,4 and verify that last dimension has value 4.
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print('shape of array: ', arr.shape)


# Reshaping 1-D array to 2-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
newarr = arr.reshape(2, 3, 2)   # conversion of 1-D into 3-D array
print(newarr)


# Can we reshape into any shape?
import numpy as np
abc = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(abc.reshape(2, 4))
#print(abc.reshape(3, 3))  --> ERROR as we don't have 9 elements


# To check if the returned array is copy or view...
import numpy as np
bcd = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(bcd.reshape(2, 4))
print(bcd.reshape(2, 4).base)


# Unknown dimension
import numpy as np
aec = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(aec.reshape(2, 2, -1))   # Use of '-1' will itself calculate the number for us


# Flattening arrays - converting multidimensional array into 1-D
import numpy as np
ar = np.array([[1, 2, 3], [4, 5, 6]])
print(ar.shape)
print(ar.reshape(-1))
