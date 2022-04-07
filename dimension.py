import numpy as np


#create 1 dimension array
arr = np.array([10,81,67,45])
print(arr[0]+arr[1])
print("printed the 1 dimension array")

# 2D array
arr = np.array([[1,2,4,67,81],[91,56,43,23,78]])
print(arr)
print("printed the 2 dimension array")
print(arr)
print(arr.ndim)

# 3d 
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr2)

# check dimension (3D array)
arr = np.array([[[1,56,41,34,45],[23,31,56,78,91]],[[23,41,56,67,87],[12,21,32,24,54]]])
print(arr)
print(arr.ndim)

# create dimension
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)



# adding it will convert int into string bcz (asciivalue) strng have higher priorty then int
arr2 = np.array([10,81,67,45,"python"])
print(arr2[0]+arr2[1])
print("printed the 1 dimension array")
# op=1081

# here float have high priorty then int
arr2 = np.array([90.0,10,81,67,45])
print(arr2[1]+arr2[2])
print("printed the 1 dimension array")