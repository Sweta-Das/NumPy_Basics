# where()
import numpy as np
arr = np.array([1, 2, 3, 7, 5, 6, 7, 7])
a = np.where(arr == 7)
print(a)

# Finding indexes that contains even values
ars = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.where(ars % 2 == 0)
print(b)

# Finding indexes that contains odd values
c = np.where(ars % 2 != 0)  # also, c = np.where(ars % 2 == 1)
print(c)

# searchsorted()
art = np.array([6, 7, 8, 9])
d = np.searchsorted(art, 7)
print(d)  # left-most index that maintains the sort order is returned

# Search from the right side
e = np.searchsorted(art, 7, side='right')
print(e)

# To search for more than one value, we use array.
aru = np.array([1, 4, 6, 8])
f = np.searchsorted(aru, [2, 3, 5, 7, 9])
print(f)
