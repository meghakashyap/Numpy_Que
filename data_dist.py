from numpy import random

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
# using probabiltiy p sum is 1(0.1+0.3+0.4+0.2)

x = random.choice([3,5,7,9],p=[0.1,0.3,0.4,0.2],size=(50))
print(x)
