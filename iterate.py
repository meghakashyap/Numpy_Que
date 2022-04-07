import numpy as np

# 1d
arr = np.array([10,81,67,45])
for i in arr:
    print(i)
    
    
# 2d
arr1 = np.array([[1,2,4,67,81],[91,56,43,23,78]])
for i in arr1:
    for x in i:
        print(x)

# 3d 
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
for x in np.nditer(arr2):
    print(x)
    
# iterate  int data into string
arr3 = np.array([1, 2, 3])
for x in np.nditer(arr3, flags=['buffered'], op_dtypes=['S']):
  print(x)
  


# Iterate through every scalar element of the 2D array skipping 1 element:
arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr4[:, ::2]):
  print(x)