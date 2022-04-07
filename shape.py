import numpy as np

# shape use to know how mnay   column and row we have
arr = np.array([10,21,30,41],ndmin=5) 
print(arr) 
print("the shape of the array is",arr.shape) 


# reshape
# making 1 dimension to 2 dimension
arr1 = np.array([10,1,78,91,23,42,51,90])
print(arr1) 
newarr=arr1.reshape(2,4)
print(newarr) 

# making 1 dimension to 3 dimension
arr2 = np.array([10,1,78,91,23,42,51,90,78,61,76,56])
print(arr2)
newarr=arr2.reshape(2,3,2) 
print(newarr) 



# reshape using -1

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)