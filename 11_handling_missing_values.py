"""numpy funcn help us handle missing values in datasets
np.isnan()->detects missing values
np.nan_to_num()
np.isinf() """

import numpy as np
#nan means not a number
arr = np.array([1, 2, np.nan, 4, np.nan])
print(np.isnan(arr)) # [False False  True False  True]

#removing missing values
removed = arr[~np.isnan(arr)]
print(removed) # [1. 2. 4.]

#replacing missing values
arr[np.isnan(arr)] = 0
print(arr) # [1. 2. 0. 4. 0.]

#np.nan_to_num(array,nan = value) np.nan_to_num()
# with 0 (or a value you choose)
# +inf → with a large finite number (default)
# -inf → with a large negative finite number

arr2 = np.array([1,2,np.nan,4,5,np.nan,7,8])
arr2 = np.nan_to_num(arr2,nan = 100) #by default if some value is not set then it will be set to 0
print(arr2)


arr = np.array([1, 2, np.nan, np.inf, -np.inf])
clean = np.nan_to_num(arr)
print(clean)  #[  1.   2.   0. 1.79769313e+308 -1.79769313e+308 ]


""" np.isinf():- returns true to infinite vals """
arr = np.array([1, 2, np.inf, -np.inf, np.nan])
print(np.isinf(arr)) #[False False  True  True False]



