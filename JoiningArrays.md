# Joining in Arrays
- Joining = putting contents of 2/more arrays in a single array.<br/>
- NumPy arrays are joined by axes.<br/>
- Sequence of arrays needed to be joined is passed through "concatenate()", along with the axis.<br/>
- If the axis isn't explicitly passed, it's taken as '0'.<br/>
<br/>

## Joining 2 Arrays
> import numpy as np<br/>
> ar1 = np.array([1,2,3])<br/>
> ar2 = np.array([4,5,6])<br/>
> arr = np.concatenate((ar1, ar2))<br/>
> print(arr)<br/>
<br/>

Output : 
> [1 2 3 4 5 6]<br/>
<br/>

## Joining 2D arrays along rows (axis = 1)
> ar1 = np.array([[1,2], [3,4]])<br/>
> ar2 = np.array([[5,6], [7,8]])<br/>
> arr = np.concatenate((ar1, ar2), axis = 1)<br/>
> print(arr)<br/>
<br/>

Output:
> [[1 2 5 6] [3 4 7 8]]<br/>

## Joining Arrays Using Stack Functions
- Stacking is the same as concatenation.
- The only difference between stacking & concatenation is that it's performed along a new axis.
- Concatenating 2 1D arrays along the 2nd axis results in putting them one over the other, i.e., stacking.
- Sequence of arrays needed to be joined is passed through "stack()" along with the axis. If axis isn't explicitly defined, it's taken as 0.
<br/>

> ar1 = np.array([1,2,3])<br/>
> ar2 = np.array([4,5,6])<br/>
> arr = np.stack((ar1, ar2), axis = 1)<br/>
> print(arr)
<br/>

Output:
> [[1 3] [2 5] [3 6]]<br/>

### Stacking along rows
- "hstack()" is used to stack along rows.<br/>
> np.hstack((ar1, ar2))<br/>

Output: 
> [1 2 3 4 5 6]<br/>

### Stacking along columns
- "vstack()" is used to stack along columns.<br/>
> np.vstack((ar1, ar2))<br/>

Output: 
> [[1 2 3] [4 5 6]]<br/>

### Stacking along height (depth)
- "dstack()" is used to stack along height.<br/>
> np.dstack((ar1, ar2))<br/>

Output: 
> [[[1 4] [2 5] [3 6]]]<br/>
<br/>

# Splitting NumPy Arrays
- Splitting is the reverse of NumPy Joining <br/>
- The array we want to split and the number of splits are passed through "array-split()". <br/>
### Splitting the array into 3 parts:
> aer = np.array([1,2,3,4,5,6]) <br/>
> new_aer = np.array_split(aer, 3) <br/>
> print(new_aer) <br/>
<br/>

Output:
> [array([1,2]), array([3, 4]), array([5, 6])] <br/>
<br/>

NOTE: If the array has fewer elements than required for splitting, it'll adjust from the end accordingly.<br/>
      split() is also available in Python but, it won't adjust the elements, when elements are less while splitting. array_split() works properly and better as compared to split(). <br/>
<br/>

## Splitting Into Arrays
- Return value of the array_split() is an array containing each of the splits as an array. <br/>
- If we split an array into 3 arrays, we can access them from the result similar to any array element. <br/>
<br/>

> print(new_aer[0]) <br/>
> print(new_aer[1]) <br/>
<br/>

Output:
> [1 2] <br/>
> [3 4] <br/>
<br/>

## Specifying axis of the split in 2D arrays
> abc = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]) <br/>
> new_abc = np.array_split(abc, 3, axis = 1) <br/>
> print(new_abc) <br/>
<br/>

Output:
> [array([[1], [4], [7], [10]]), array([[2], [5], [8], [11]]), array([[3], [6], [9], [12]])] <br/>
<br/>

NOTE: We can also use np.hsplit(abc, 3) to get the same result. <br/>
<br/>

### Splitting using np.hstack()
> print(np.hstack(abc)) <br/>

Output:
> [1 2 3 4 5 6 7 8 9 10 11 12] <br/>
<br/>

NOTE: Similarly, we can also split using vstack(), dstack() and vsplit(). <br/>
<br/>


