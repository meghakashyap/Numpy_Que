import numpy  as np

# copy is working as deep copy
a = np.array([2,4,6])
x= a.copy()
print(x)

a[0:2]=[9,7]
print(a)

# view is working as a shallow copy
arr = np.array([3,4,5])
b = arr.view()
print(b)
b[0] = 78
print(b)
print(arr)


arr1 = np.array(["a","b","cat"])
b = arr1.view()
print(arr1[1])
arr1[1] ="dog"
print(arr1)


# base is used to check that copy and view owns the data  or not
arr =np.array([10,11,8,5,0]) 
x = arr.copy()
y = arr.view()
print(x.base) 
print(y.base) 