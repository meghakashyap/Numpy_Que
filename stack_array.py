import numpy as np

# . How to stack two arrays vertically?
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

# method1
adding = np.concatenate([a,b],axis=0)
print(adding)

# method12
using_stack = np.vstack([a, b])
print(using_stack)


# . How to stack two arrays horizontally

h_stack = np.hstack([a,b])
print(h_stack)