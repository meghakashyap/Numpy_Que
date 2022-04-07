import numpy as np

# 2D array
arr = np.array([[1,2,4,67,81],[91,56,43,23,78]])
print(arr)
print("printed the 2 dimension array")
print(arr[1:2][0,0])
print(arr.ndim)
# [[91 56 43 23 78]]


#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])


# From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])