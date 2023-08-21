# Sorting Arrays
- Sorting = putting elements in an ordered sequence (like numeric, alphabetic, ascending, descending, etc.)
- sort() -> function of NumPy ndarray object, that sorts a specified array
<br/>

> ab = np.array([5, 3, 4, 0, 2, 1]) <br/>
> print(np.sort(ab))
<br/>

Output:
> [0 1 2 3 4 5] <br/>

**NOTE:** sort() returns a copy of the array, leaving the original array unchanged.
## Sorting alphabetically
> ac = np.array(['pear', 'banana', 'apple', 'mango'])<br/>
> np.sort(ac) <br/>
<br/>

Output
> ['apple', 'banana', 'mango', 'pear']<br/>
<br/>

## Sorting boolean array
> ad = np.array([True, False, True, True, False, False])<br/>
> np.sort(ad)<br/>
<br/>

Output:
> [False False False True True True]<br/>

## Sorting 2D Array
> ae = np.array([[21, 10, 3], [8, -6, 4], [3, 0, -2]])<br/>
> np.sort(ae)<br/>
<br/>

Output:
> [[3 10 21] [-6 4 8] [-2 0 3]]
