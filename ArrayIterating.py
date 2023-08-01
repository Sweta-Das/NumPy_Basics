import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
    print(x)   # 1-D array; each element is displayed

#Iterating 2-D array
import numpy as np
abc = np.array([[1, 2, 3], [4, 5, 6]])
for x in abc:
    print(x)   # 2-D array; each row is displayed

#To obtain actual values
import numpy as np
abc = np.array([[1, 2, 3], [4, 5, 6]])
for x in abc:
    for y in x:
        print(y)

#Iterating 3-D array
import numpy as np
abd = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in abd:
    print(x)

# To show iteration clearly.
for x in abd:
    print("x represents the 2-D array:")
    print(x)

# To return actual values
for x in abd:
    for y in x:
        for z in y:
            print(z)
