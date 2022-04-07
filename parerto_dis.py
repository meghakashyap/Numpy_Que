#zipf Distribution # are is 2nd most word in this paragraph # 1/2 is the common usage of are in whole english from numpy import random x = random.zipf(a=2, size=(2, 3)) print(x) #Pareto Distribution # Pareto's law : #20% factors cause 80% outcome # a -shape parameter # size= x = random.pareto(a=2,size=(2,3)) print(x) #Rayleigh Distribution #scale standard deviation # size(shape) from numpy import random #x = random.rayleigh(scale=2, size=(2, 3)) x = random.rayleigh(size=6) print(x) 


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i)
  z.append(j)
print(z)