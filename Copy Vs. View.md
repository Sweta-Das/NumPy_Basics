# Copy Vs. View 
Copy means a new array in NumPy. Any changes made to the copy don't affect the original array, and vice-versa. Also, copies own its data.<br/>
View is just a view of the original array. Any changes made to the view will affect the original array, and vice-versa. View doesn't own the data.<br/>
<br/>
To make a copy of an array:<br/>
> arr.copy() <br/>
<br/>
To make a view of an array:<br/>
> arr.view() <br/>
<br/>
To check if an array owns its data:<br/>
> arr = np.array([1,2,3,4,5]) 
> x = arr.copy()
> y = arr.view()
> print(x.base)
> print(y.base)
<br/>
Output of copy:<br/>
> None
Output of view:<br/>
[1 2 3 4 5]<br/>
