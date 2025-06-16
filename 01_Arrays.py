py_list = [1,2,3,4,5]
print(py_list) # this will print with the commas

import numpy as np
# 1-D array
numpy_array = np.array([1,2,3,4,5])  #np.([li1,li2,li3]) this function converts list to array
print(numpy_array)   # this will print without the commas

# 2-D array
numpy_array2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(numpy_array2D)

# multi-dimentional array :- contains

#if we want to set any default value to whole array

arr1 = np.zeros(3)   # default value = 0, size =3
print(arr1)

arr2 = np.ones(5)   #deafult value = 1, size = 5 
print(arr2)

# for 2d array
arr3 = np.ones((2,3))  # 2*3 size array
print(arr3)

# if we want to give array value other than 0,1
arr4 = np.full((2,2),7)  #size = 2*2 , val = 7
print(arr4)


#creating sequence of numbers in numpy, we use arange() function, 
#syntax :- arange(start,stop,steps)
arr5 = np.arange(1,10,2)
print(arr5)    # o/p:- [1 3 5 7 9]

# creating identity matrix : 1 in diagonal and 0 elsewhere
arr6 = np.eye(4) #size
print(arr6)
