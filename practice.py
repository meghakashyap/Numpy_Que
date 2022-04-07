import numpy as np

arr = np.array([1,4,3,5,6])
print(type(arr))
print(arr)

a = np.array({"a":1,"b":2,"c":3})
print(type(a))

t = np.array(("1","A","2"))
print(t)


#create 0 dimension array

import numpy as np

arr = np.array('bha54654846565rti')
print(arr)
print("printed the 0 dimension array")



arr=np.array(["1","2","3"])
n=arr.astype("i")
print(n)
n[2]="a"
print(n)