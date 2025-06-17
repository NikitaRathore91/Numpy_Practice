#  fancy indexing allows to access multiple array elements at once using lists or arrays of indices, instead of just slices.
import numpy as np
arr1 = np.array([10,20,30,40])
print(arr1[[1,2,3]])
index = [0,1,2]
print(arr1[index])

#with 2d 
arr2 = np.array([[11, 12],[21, 22],[31, 32]])
print(arr2[[0, 2]])
rows = [0,1]
col = [1,0]
print(arr2[rows,col])   #o/p : [12,21]



#   BOOLEAN MASKING (FILTERING)
arr3 = np.array([5,10,15,20])
mask = arr3>10
print(mask) #o/p :- [ False,False,True,True]
print(arr3[mask])  #o/p :- [15 20]