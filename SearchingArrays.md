# Searching Arrays
- Array can be searched to look for a certain value. <br/>
- Searching any array in NumPy returns the indexes of the place where the given value is present. <br/>
- where() <br/>
<br/>

## Search Sorted
- searchsorted() is another NumPy array function that performs the binary search in an array.
- returns index where the specified value would be inserted to maintain the search order
- assumed to be used on sorted arrays
- By default, it returns the left-most index <br/>
<br/>

### Searching From the Right side
- To return right-most index, <br/>
> np.searchsorted(array, No. to search, side= 'right')
<br/>

### Searching for multiple values
- To search for multiple values in an array, an array with specified values is provided. <br/>
> arr = np.array([1,4,6,8]) <br/>
> np.searchsorted(arr, [1, 2, 3, 4, 6]) <br/>

Since, 2 & 3 both values are missing from the array hence, both will be inserted between 1 & 4, and the output will be; <br/>
Output:
> [1 1 2 3 4]
  
