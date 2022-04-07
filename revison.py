import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# data distribution
x = random.choice([2,3,4,5,1],p=[0.1,0.2,0.4,0.0,0.3],size=(10))
# print(x)

# Random permutation
a = np.array([1,2,3])
random.shuffle(a)
# print(a)

# print(random.permutation(a))

# seaborn
# sns.distplot(a,hist=True)
# plt.show()


# normal dis
n = random.normal(loc=1,scale=2,size=(5))
# print(n)

# sns.distplot(n,hist=True)
# plt.show()

# bionomial
# b = random.binomial(n=3,p=0.5,size=(5))
# print(b)
# sns.distplot(b,hist=True)
# plt.show()

# x = random.poisson(lam=2, size=10)
# print(x)


x = random.multinomial(n=5, pvals=[1/6, 1/6, 1/6, 1/6, 1/6])
print(x)
