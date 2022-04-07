import numpy as np

# 5. How to replace items that satisfy a condition with another value in numpy array?

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[arr % 2 != 0] = -1
print(arr)


# 6. How to replace items that satisfy a condition without affecting the original array?

data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(data % 2 == 1, -1, data)
print(out)

new_data = data.copy()
new_data[new_data % 2 != 0]  = -1
print(new_data)