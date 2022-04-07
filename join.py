import numpy as np

# concatenate  
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6]) 
arr = np.concatenate((arr1,arr2)) 
print(arr) 

# stack with axis=0  joining horizontally(row) bydefault  axis is 0
arr1 = np.array([[1, 2], [3, 4]]) 
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0) 
print(arr) 

# stack with axis=1  joining vertically (column)
arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6]) 
arr = np.stack((arr1, arr2),axis=1) 
print(arr) 

# hstack for joinig array  horizontally(row)
arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6]) 
arr = np.hstack((arr1, arr2)) 
print(arr) 

# vstack for joinig array  vertically(column)
arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr) 

# dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)