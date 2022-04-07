import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

# Method 1:
index = np.where((a>=5) & (a<=10))
print(a[index])


# Method 2:
index = np.where(np.logical_and(a>=5, a<=10))
print(a[index])
#> (array([6, 9, 10]),)

# Method 3: (thanks loganzk!)
b = a[(a >= 5) & (a <= 10)]
print(b)