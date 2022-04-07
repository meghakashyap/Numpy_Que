import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7] 
z = [] 
for i, j in zip(x, y):
    z.append(i + j) 
print(z) 

# 2nd way
z = np.add(x,y)
print(z) 


# in python
x = [1, 2, 3, 4]
y = [4, 5, 6, 7] 
z=[]
i=0
while i <len(x):
    a = x[i]+y[i]
    z.append(a)
    i+=1
print(z)