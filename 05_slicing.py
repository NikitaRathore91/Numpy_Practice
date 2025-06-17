#slicing : Slicing means selecting a range of elements 
#syntax : array[start:stop:step]   start is included,stop is excluded

import numpy as np
arr1 = np.array([10,20,30,40,50,60])
print(arr1[1:5]) #o/p: [20 30 40 50]
print(arr1[1:6:2]) #o/p: [20,40,60]
print(arr1[:4]) # [10 20 30 40]
print(arr1[:6:2]) #[10 30 50]
print(arr1[::2]) # [10 30 50]
print(arr1[-5:-1]) # [20 30 40 50]
print(arr1[6:0:-1]) #[60 50 40 30 20]
print(arr1[::-1]) # [60 50 40 30 20 10]



