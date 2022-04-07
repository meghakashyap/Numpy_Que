import numpy as np 

arr = np.array([41, 42, 43, 44]) 
new_arr=arr>42 
print(new_arr) 
arr = arr[new_arr] 
print(arr)


# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x
print(newarr)


# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)