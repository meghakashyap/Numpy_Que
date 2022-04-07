import numpy as np

# 4. How to extract items that satisfy a given condition from 1D array
data = np.array([1,2,3,5,6,8,9,13])
odd_n = data[data % 2 != 0]
print(odd_n)

# finding even number
even_n = data[data % 2 == 0]
print(even_n)