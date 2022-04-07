import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

i = 0
l  = []
arr = []
while i < len(a):
    for j in b:
        if a[i] == j:
            l.append(i)
    i+=1

print(l)   

# preferred way
arr = np.where(a == b)
print(arr)