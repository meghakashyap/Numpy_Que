import numpy as np

# 11. How to get the common items between two python numpy arrays?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

item = np.intersect1d(a,b)
print(item)


# 12. How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# From 'a' remove all of 'b'
remove_item = np.setdiff1d(a,b)
print(remove_item)