# NumPy automatically stretches or repeats a smaller array so it can match the shape of a bigger one for math operations like +, -, *, etc.
# arr = np.array([1, 2, 3])
# result = arr + 10
# NumPy automatically turns 10 into [10, 10, 10] behind the scenes.

import numpy as np
prices = np.array([100,150,200,250,300])
discount = prices*9/10  # deducing a discount of 10% from original price
print(discount)

""" RULES OF BROADCASTING
    HOW NUMPY MANAGES DIMENSIONS
    1)matching dimension 
    eg:- [1,2,3] + [4,5,6] will give [5 7 9]
    2)expanding single elements
    3)incompatible shapes eg :- [1,2,3]+[2,3] will give error
    
"""

#expanding single dimesions   
a = np.array([1,2,3])
b = np.array([10])
ans = a+b
print(ans)  #0/p :- 11 12 13

#Adding 2D and 1D array
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b     # o/p :- [[11,22,33][14 25 36]]

# 2D Array + 1D Column Vector
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[10],
              [20]])

result = a + b
print(result)   #o/p[[11 12 13][24 25 26]]


