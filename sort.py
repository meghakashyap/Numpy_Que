import numpy as np 

# sorting 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) 

# sorting boolean array
arr = np.array([True, False, True]) 
print(np.sort(arr)) 

# sorting String  array
arr = np.array(['banana', 'cherry', 'apple']) 
print(np.sort(arr))

# sorting 1D array and checking theid
arr = np.array([3, 2, 0, 1]) 
print(id(arr)) 
x = np.sort(arr) 
print(id(x)) 