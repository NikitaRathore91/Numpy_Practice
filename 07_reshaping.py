# Reshaping means changing the shape (rows & columns) of a NumPy array without changing its data
import numpy as np
"""
reshape(rows,columns) specify new shape
if dimensions match   
"""
arr1 = np.array([1,2,3,4,5,6])
arr2 = arr1.reshape(2,3)
print(arr2)   # [[1 2 3] [4 5 6]]

#reshaping never returns a copy, it returns a view, it means it will affect original array 

#FLATTENING OF ARRAY :- ravel() ,flatten() when we want to convert multi dimension array to 2d,1d
# .ravel() :- it creates a view , can affect/change original array
#.faltten() :- it creates a copy, doesn't affect/change original array
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3.ravel())   #o/p:-[1 2 3 4 5 6]
print(arr3.flatten()) #o/p:- [1 2 3 4 5 6]

