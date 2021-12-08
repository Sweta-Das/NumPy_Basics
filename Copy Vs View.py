# copy()

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

#########################################################
# view()

import numpy as np
aa = np.array([11, 22, 33, 44, 55])
y = aa.view()
aa[0] = 21
print(aa)
print(y)

########################################################
# Making changes in the view() variable

y[1] = 23   # change in variable with view() also affects original array
print(aa)
print(y)

#######################################################
# base attribute

import numpy as np
ab = np.array([10, 20, 30, 40, 50])
a = ab.copy()
b = ab.view()
print(a.base)   # copy owns data; returns 'None'
print(b.base)   # view doesn't own data; returns original object
