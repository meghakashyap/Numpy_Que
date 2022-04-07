from numpy import random
import numpy as np
from pandas import array

arr=np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

print(random.permutation(arr))