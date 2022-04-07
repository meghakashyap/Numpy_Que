from numpy import random

x=random.randint(100)
print(x)
# 0 to 100

#pure float number
#0 to 1
x = random.rand()
print(x)

# creating 1 dimension
x = random.randint(100,size=5)
print(x)

# creating multi dimnesion
x = random.randint(100,size=(3,5))
print(x)


x = random.rand(3,5)
print(x)


# random  num choose by yourself
x = random.choice([3,5,7,9])
print(x)

