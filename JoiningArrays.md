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


