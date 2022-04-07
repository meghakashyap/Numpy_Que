import numpy as np 

# The searchsorted() method is assumed to be used on sorted arrays
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, [2,5,8]) 
print(x) 


# Find the indexes where the value 7 should be inserted, starting from the right:
arr = np.array([6, 7, 8, 9]) 
x = np.searchsorted(arr, 7,side='right') 
print(x) 


# Find the indexes where the value 7 should be inserted, starting from the left (default its left)
arr = np.array([6, 7, 8, 9]) 
x = np.searchsorted(arr, 7,side='left') 
print(x) 

# Find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0) 
print(x) 