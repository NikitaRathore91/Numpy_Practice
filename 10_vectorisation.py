""" Vectorization means performing operations on entire arrays 
(vectors, matrices) without using loops — just like doing math directly."""
import numpy as np

#without vectorisation
arr = np.array([1, 2, 3, 4])
squared = []

for i in arr:
    squared.append(i ** 2)

print(squared)

#with vectorisation
arr = np.array([1, 2, 3, 4])
squared = arr ** 2
print(squared)  #[ 1  4  9 16 ]


#add 2 arrays 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b  # vectorized addition
print(c)  #[5 7 9]


