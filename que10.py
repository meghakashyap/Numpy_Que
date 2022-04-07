import numpy as np

# 10. How to generate custom sequences in numpy without hardcoding
a = np.array([1,2,3])
arr = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(arr)