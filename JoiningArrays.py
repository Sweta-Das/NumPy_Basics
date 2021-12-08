import numpy as np
ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 5, 6])
arr = np.concatenate((ar1, ar2))
print(arr)

# Joining 2-D arrays
ary1 = np.array([[1, 2], [3, 4]])
ary2 = np.array([[5, 6], [7, 8]])
ary = np.concatenate((ary1, ary2), axis=1)
print(ary)

# Joining arrays with stack
ar = np.stack((ar1, ar2), axis=1)
print(ar)

ab = np.hstack((ar1, ar2))  # stacking along rows
print(ab)

ac = np.vstack((ar1, ar2))  # stacking along columns
print(ac)

ad = np.dstack((ar1, ar2))  # stacking along height (or, depth)
print(ad)


# Splitting Arrays

aer = np.array([1, 2, 3, 4, 5, 6])
new_aer = np.array_split(aer, 3)  # splitting arrays in 3 parts
print(new_aer)
new_aer = np.array_split(aer, 2)  # splitting arrays in 2 parts
print(new_aer)

naer = np.array([1,2,3,4,5,6,7])
new_aer = np.array_split(naer, 3)  # splitting arrays in 3 parts
print(new_aer)
new_aer = np.array_split(naer, 2)  # splitting arrays in 2 parts
print(new_aer)

#Splitting array in 4 parts
are = np.array([1, 2, 3, 4, 5, 6])
new_are = np.array_split(are, 4)
print(new_are)

#Splitting into arrays

arc = np.array([1, 2, 3, 4, 5, 6])
new_arc = np.array_split(arc, 3)
print(new_arc[0])
print(new_arc[1])
print(new_arc[2])

# Splitting 2-D Arrays
ard = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_ard = np.array_split(ard, 3)
print(new_ard)

arf = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arf = np.array_split(arf, 3)
print(new_arf)

# Specifying axis of split in 2-D arrays
arh = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arh = np.array_split(arh, 3, axis=1)
print(new_arh)

print(np.hsplit(arh, 3))  # horizontal splitting
print(np.hstack(arh))
print(np.vstack(arh))
print(np.dstack(arh))
print(np.vsplit(arh, 3))

