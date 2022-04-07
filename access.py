import numpy as np

# Access the third element of the second array of the first array: 
arr = np.array([[[1,56,41,34,45],[23,31,56,78,91]],[[23,41,56,67,87],[12,21,32,24,54]]]) 
# positive indexing
print(arr[1][0][2])
print(arr[1,0,2]) 

# negative indexing
print(arr[-1,-2,-3])
print(arr[-1][-2][-3])

# uisng slicing
print(arr[1:2][0][0,2])