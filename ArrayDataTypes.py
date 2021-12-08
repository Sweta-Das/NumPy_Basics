import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)   # array with integer values

aa = np.array(['a', 'bloom', 'con'])
print(aa.dtype)   # array with strings

###########################################################
# Creating arrays with defined data types

import numpy as np
ab = np.array([1, 2, 3, 4], dtype = 'S')  # specifying that array should be of 'string' type
print(ab)
print(ab.dtype)

ac = np.array([6, 7, 8, 9], dtype='i4')
print(ac)
print(ac.dtype)

##########################################################
# Value Error

#ad = np.array(['a', '2', '3'], dtype='i')
# print(ad)   # ValueError

##########################################################
# Converting Data Type on Existing Arrays 'astype()'

import numpy as np
ae = np.array([1.1, 2.2, 3.3])
newae = ae.astype('i')   # also, ae.astype('int')
print(ae)
print(ae.dtype)
print(newae)
print(newae.dtype)

newar = ae.astype(bool)
print(newar)
print('\n')

af = np.array([1, 0, 3])
newaf = af.astype(bool)
print(af)
print(newaf)
print(newaf.dtype)

