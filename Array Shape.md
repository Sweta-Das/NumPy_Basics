# Shape of an Array
Shape of an array is the number of elements in each dimension.<br/>
<br/>
To print the shape of 2D array:<br/>
<br/>
> arr = np.array([[1,2,3],[4,5,6]]) <br/>
> print(arr.shape) <br/>
<br/>
Output: (2,4) <br/>
<br/>
The output shows that the array has 2 dimensions, where 1st dimension has 2 elements and 2nd dimension has 4 elements.<br/>
<br/>

# Reshaping Arrays
Reshaping means changing the dimensions or changing the number of elements in each dimension in an array.<br/>
<br/>
To reshape 1D to 2D: <br/>

> arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) <br/>
> newarr = arr.reshape(4, 3) <br/>

<br/>
Output: [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]] <br/>
<br/>
We can also reshape from 1D to 3D.<br/>
As long as the elements required for shaping are equal in both shapes. We can reshape into any shape. <br/>
A 1D 8-element array can be reshaped into a 2D 4-element array, but we can't reshape it into a 3D 3-element array because it'll require 9 elements.<br/>
<br/>

## Unknown dimension while reshaping
NumPy allows to have one unknown dimension while reshaping. It means we don't have to specify an exact number of dimensions. We can simply pass "-1".<br/>
> arr.reshape(2,2,-1)<br/>

## Array Flattening
It means converting a multidimensional array into a 1D array.<br/>
> arr.reshape(-1)

