# We can calculate shape,size and dimension  
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6]])

#shape :- tells us total rows and column
print(arr1.shape)   # o/p :- (5,)  
print(arr2.shape)   # o/p :- (2,3)  (row,column)

#size :- total elements
print(arr1.size)    #o/p :- 5
print(arr2.size)    #o/p :- 6

# ndim :- number of dimensions
print(arr1.ndim)    #o/p :- 1
print(arr2.ndim)    #o/p :- 2

# dtype :- tells us about data type of element
print(arr1.dtype)
arr3 = np.array(["abc","nikita"])  
arr4 = np.array([1,"abc",9.87])
arr5 = np.array(["abc","Nikita Rathore"])
arr6 = np.array([1,2,3.3])
print(arr3.dtype)  #o/p :- <U6   where U:- unicode string and 6:- maxlength 6
print(arr4.dtype)  #o/p :- <U32  
print(arr5.dtype)  #o/p :- <U14
print(arr6.dtype)  #o/p :- float64


#DATATYPE CONVERSION
#syntax :- array.astype(new.type)
arr7 = np.array([1.2,2.2,3.2])
arr8 = arr7.astype(int)
print(arr8)   #o/p:- [1,2,3]
print(arr8.dtype) #o/p:- int64