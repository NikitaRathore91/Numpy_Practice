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


""" APPEND() 
np.append(array,valuess,axix = none)
"""
# append in 1D(default axix = none)
arr4 = np.array([1,2,3])
new_arr4 = np.append(arr4,[4,5])
print(new_arr4) # o/p:- [1 2 3 4 5]

# append in 2D, axis = 0
arr5 = np.array([[1,2],[3,4]])
new_arr5 = np.append(arr5,[[5,6]],axis = 0) 
print(new_arr5)  #o/p:- [[1 2][3 4][5 6]]

#append in 2D, axix = 1
arr6 = np.array([[1,2],[4,5]])
new_arr6 = np.append(arr6,[[3],[6]],axis = 1)
print(new_arr6) #o/p:- [[1 2 3][4 5 6]]


""" CONCAT()
np.concatenate((array1, array2, ...), axis=0)
"""

#concatinate 1D arrays(default axis = 0)
a = np.array([1,2])
b = np.array([3,4])
c = np.concatenate((a,b))
print(c)  #o/p :- [1 2 3 4]

#concatenate 2D arrays (row wise, axis = 0)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c = np.concatenate((a,b),axis = 0)
print(c) #o/p :- [[1 2][3 4][5 6]]

#concatenate 2D array (col wise, axis = 1)
a = np.array([[1,2],[3,4]])
b = np.array([[5],[6]])
c = np.concatenate((a,b),axis = 1)
print(c)  #o/p :- [[1 2 5][3 4 6]]

""" DELETE
np.delete(array,index,axis = none)
"""

# Delete from 1D Array(No axis)
a1 = np.array([10,20,30,40])
new_a1 = np.delete(a1,2)
print(new_a1) #o/p :- [10 20 40]

# Delete a row from 2D Array (axis = 0)
b1 = np.array([[1,2],[3,4],[5,6]])
new_b1 = np.delete(b1,1, axis = 0)
print(new_b1) #o/p :- [[1 2][5 6]]

#Delete a col from 2D Array
c1 = np.array([[1,2,3],[4,5,6]])
new_c1 = np.delete(c1,2,axis =1)
print(new_c1) #o/p :- [[1 2][4 5]]


""" 
functions to stack arrays vertically, horizontally, or depth-wise.
"""
# np.vstack() - vertical stack (row wise)
a = np.array([1,2])
b = np.array([3,4])

result = np.vstack((a,b))
print(result)  # [[1 2][3 4]]

# np.hstack()
a = np.array([1,2])
b = np.array([3,4])
result = np.hstack((a,b))
print(result)  #o/p :- [1 2 3 4]

#np.stack()
a = np.array([1,2])
b = np.array([3,4])
result = np.stack((a,b), axis = 0)
print(result) #o/p :- [[1 2][3 4]]

result = np.stack((a,b), axis = 1)
print(result) #o/p :- [[1 3][2 4]]

#np.dstack() -> stack depth wise(3D arrays)
a = np.array([1,2])
b = np.array([3,4])
result = np.dstack((a,b))
print(result) #o/p :- [[[1 3][2 4]]]

""" SPLIT
1.np.split()	Split array into equal parts
2.np.array_split()	Split into unequal parts (flexible)
3.np.hsplit()	Split horizontally (columns)
4.np.vsplit()	Split vertically (rows)
"""
#np.split()
arr = np.array([1,2,3,4,5,6])
parts = np.split(arr,3) # 3 equal parts
print(parts) # o/p:- [array([1, 2]), array([3, 4]), array([5, 6])]
# Error: array not divisible by 4

#np.array_split()
arr = np.array([1, 2, 3, 4, 5])
parts = np.array_split(arr, 2)
print(parts)

#np.hsplit()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
parts = np.hsplit(arr, 2)
print(parts)

#np.vsplit()
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
parts = np.vsplit(arr, 2)
print(parts)

