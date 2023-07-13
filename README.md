## NumPy or Numerical Python
It is a Python library that supports large, multi-dimensional arrays & matrices and a wide range of mathematical functions to operate on these arrays. It was created by Travis Oliphant in 2005. It is designed to be fast and efficient for performing numerical computations & mathematical functions for operations such as; <br/>
- Array manipulation<br/>
- Linear Algebra<br/>
- Fourier Transform<br/>
- Random Number Generation, and many more.<br/><br/>

![download](https://github.com/Sweta-Das/NumPy_Basics/assets/73231461/6b897bd5-438d-4603-a5d3-4200aec491f7)
<br/><br/>

### Importing NumPy in Python
To utilize NumPy in our code, we need to import it by adding the following line at the beginning of the script:
>import numpy as np

### NumPy Array Indexing
1D Arrays<br/>
It's the same as accessing any array element. We can access any array element through its index number. The indexes in Python start with 0.<br/>
>arr = np.array([1,2,3,4])<br/>

2D Arrays<br/>
To access 2D arrays, comma-separated integers representing the dimension & the index of the element are used. The dimension represents the rows & index represents the column.<br/>
>arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])<br/>

To access any element from say, 3rd element from 2nd row:<br/>
>print(arr[1,2])

>8<br/>

3D Arrays<br/>
To access 3D arrays, we can further extend the comma-separated integers.<br/>
>arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])<br/>

To access 3rd element of the 2nd array of the 1st array:<br/>
>print(arr[0,1,2])

>6

0 => 1st dimension that contains 2 arrays: [[1,2,3], [4,5,6]] & [[7,8,9], [10,11,12]], with 0 it'll choose [[1,2,3], [4,5,6]]<br/>
1 => 2nd dimension that contains 2 arrays: [1,2,3] & [4,5,6], with 1 it'll choose [4,5,6]<br/>
2 => 3rd dimensions that contains 3 values: 4,5 & 6, with 2 it'll choose 6<br/>
<br/>
Negative Indexing<br/>
Using negative indexing to access the array elements from the end.
