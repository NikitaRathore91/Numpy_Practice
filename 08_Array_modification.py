#Inserting new values 
#Updating existing values 
#Deleting elements
#Appending or Extending Arrays
"""
INSERT
np.insert(array,index,value,asix=None)
array - original array
index - index we want to insert
value - value we want to insert
axis - 
axis = 0, row-wise    # axis = none ->insert flattenend(1D), axis = 0 -> insert row wise(in a 2D array) , axis = 1 ->
1 column wise
"""
import numpy as np
# insert in 1D (no axis)
arr1 = np.array([1,2,4,5,6])
new_arr1 = np.insert(arr1,2,3)
print(new_arr1)   #o/p:- [1 2 3 4 5 6]

#insert in 2D , insert row (axis = 0)
arr2 = np.array([[10,20],[50,60]])
new_arr2 = np.insert(arr2,1,[30,40],axis = 0)
print(new_arr2)   #o/p :- [[10 20][30 40][50 60]]

#insert in 2D, insert column(axis = 1)
arr3 = np.array([[1,2],[4,5]])
new_arr3 = np.insert(arr3,2,[3,6],axis = 1)
print(new_arr3) #o/p :- [[1 2 3][4 5 6]]

