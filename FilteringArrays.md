# Filtering Arrays
- Filtering arrays means extracting some elements out of an existing array & creating a new array out of them.
- In the NumPy array, an array is filtered using a boolean index list.
- Boolean Index List = list of boolean corresponding to indexes in the array.
- Value at index:<br/>
  True -> element is contained in the filtered array <br/>
  False -> element is excluded from the filtered array <br/>
> arr = np.array([60, 61, 62, 63, 64, 65])<br/>
> a = [True, False, False, True, True, True]<br/>
> newa = arr[a]<br/>
> print(newa)<br/>
<br/>

Output:
> [60 63 64 65]<br/>
<br/>

**NOTE:** New filter containing only the values where filter array had "True" value is created.<br/>
<br/>

- Generally, without the above-given hard coding, arrays are filtered using conditions as shown on the code page.
