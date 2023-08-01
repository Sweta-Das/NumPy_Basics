# Copy Vs. View 
Copy means a new array in NumPy. Any changes made to the copy don't affect the original array, and vice-versa. Also, copies own its data.<br/>
View is just a view of the original array. Any changes made to the view will affect the original array, and vice-versa. View doesn't own the data.<br/>
<br/>
To make a copy of an array:<br/>
>arr.copy()
<br/>
To make a view of an array: <br/>

>arr.view()
<br/>
To check if an array owns its data:<br/>

> arr = np.array([1,2,3,4,5]) <br/>
> x = arr.copy() <br/>
> y = arr.view() <br/>
> print(x.base) <br/>
> print(y.base) <br/>

Output of copy:<br/>

> None<br/>

Output of view:<br/>
[1 2 3 4 5]<br/>
