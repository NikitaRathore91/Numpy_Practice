import numpy as np

arr1 = np.array([1,2,3])

print(arr1+4)  #o/p:- [5 6 7]
print(arr1*3)  #o/p:- [3 6 9]
print(arr1**2)  #o/p:- [1 4 9]

# Aggregate function :-aggregate functions are built-in functions that summarize or combine data in arrays — 
# usually by reducing multiple values into a single result (like a sum, mean, min, etc.).

arr2 = np.array([10,20,30,40,50])

print(np.sum(arr2))   #total sum
print(np.mean(arr2))  #mean of array
print(np.min(arr2))   #min element of array
print(np.max(arr2))   #max element of array
print(np.std(arr2))   #standard deviation of array
print(np.var(arr2))   #variance of array
