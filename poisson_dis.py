from numpy import random 
x = random.poisson(lam=2, size=10)
print(x) 
#0 1 2 3 4 5 6 7 8 9 
# op/-[3 2 3 8 2 0 3 1 3 2]
# isme 3 lam se  jyada 4 bar hai
# isme 2 lam se  jyada 3 bar hai
# so on..


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()