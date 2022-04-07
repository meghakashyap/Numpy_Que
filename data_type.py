import numpy as np 

# type casting
arr = np.array([1,0,3]) 
newarr = arr.astype(bool) 
print(newarr)
print(newarr.dtype)

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD" 
# integer - used to represent integer numbers. e.g. -1, -2, -3 
# float - used to represent real numbers. e.g. 1.2, 42.42 
# boolean - used to represent True or False. 
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j 
# i - integer
# b - boolean
# U - unsigned integer 
# f - float
# c - complex float 
# m - timedelta()
# M - datetime 
# O - object 
# S - string 
# U - unicode string 
# V - fixed chunk of memory for other type ( void ) 


arr= np.array([10,1,28,91],dtype='c') 
print(arr) 
print(arr.dtype) 

f = np.array([10,1,28,91],dtype=bool) 
print(f)
print(f.dtype)

f = np.array(["10","1","28","91"],dtype='i') 
print(f)
print(f.dtype)


arr = np.array([1,0,3]) 
newarr = arr.astype(float) 
print(newarr)
print(newarr.dtype)

arr= np.array([10,1,28,91],dtype='c') 
print(arr) 
print(arr.dtype) 


arr = np.array([1,0,3]) 
newarr = arr.astype("c") 
print(newarr)
print(newarr.dtype)
# [b'1' b'0' b'3']
# |S1