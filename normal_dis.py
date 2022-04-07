import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x =random.normal(size=(2,3))
print(x)


#Continuous Distribution
# 170Cm,155Cm,160
sns.distplot(random.normal(size=1000), hist=True)
plt.show()


# binomial  and normal
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=True, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=True, label='binomial')

plt.show()
