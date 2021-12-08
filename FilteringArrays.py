# Filtering arrays means creating a new array out of the existing array.
import numpy as np
arr = np.array([60, 61, 62, 63, 64, 65])
a = [True, False, True, True, False, True]
newa = arr[a]
print(newa)

# Creating a filter array that will return only values higher than 62.
ab = np.array([60, 61, 62, 63, 64, 65])
filter_ab = []  # creating an empty list

for element in ab:
    if element > 62:
        filter_ab.append(True)
    else:
        filter_ab.append(False)

new_ab = ab[filter_ab]
print(filter_ab)
print(new_ab)


# Creating filter array that will return only even elements from the original array.
import numpy as np
ac = np.array([1, 2, 3, 4, 5, 6, 7])
filter_ac = []

for element in ac:
    if (element % 2 == 0):
        filter_ac.append(True)
    else:
        filter_ac.append(False)

new = ac[filter_ac]
print(filter_ac)
print(new)

# Creating a filter array that will return only values higher than 62.
ad = np.array([60, 61, 62, 63, 64, 65])
filter_ad = ad > 62
new_ad = ad[filter_ad]
print(filter_ad)
print(new_ad)

# Creating a filter array that will return only even elements from the original array.
ae = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_ae = ae % 2 == 0
new_ae = ae[filter_ae]
print(filter_ae)
print(new_ae)
