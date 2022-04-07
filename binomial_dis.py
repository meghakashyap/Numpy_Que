
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Discrete Distribution => Yes/No,Head/Tail
#Binomial Distribution

# n = number of trials
# probability
# size


x = random.binomial((100),p=0.5,size=3)
print(x)


x = random.binomial(n=10, p=0.5, size=1000)
print(x)

sns.distplot(random.binomial(n=10, p=0.5, size=1000), kde=False)
plt.show()



sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=True, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=True, label='binomial')
plt.show()