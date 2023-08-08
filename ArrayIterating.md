# Array Iteration in Python
- Iterating means going through elements one by one. <br/>
- While dealing with multi-dimensional arrays in Numpy, we can perform the basic "for" loop of Python. <br/>
<br/>

## Iterating 1D Array

> import numpy as np<br/>
> arr = np.array([1,2,3])<br/>
> for x in arr:<br/>
>     print(x)<br/>
<br/>

In a 1D array, iteration goes through each element one by one.
## Iterating 2D Array

> ab = np.array([[1,2,3], [4,5,6]])<br/>
> for x in ab:<br/>
> print(x)<br/>
<br/>

In a 2D array, iteration goes through all of the rows.<br/>
<br/>

## Iterating 3D Array

> abc = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])<br/>
> for x in abc:<br/>
> print(x)<br/>
<br/>

In a 3D array, iteration will go through all 2D arrays.<br/>
<br/>
NOTE: If we iterate on an n-D array, it'll go through (n-1)th dimension one by one.<br/>
