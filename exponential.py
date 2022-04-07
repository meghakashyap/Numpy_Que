# exponential Distribution # scale inverse of rate # size # 1 min = 60 s # 0 sec to 60 sec # 1st person 23 sec # 2nd person 54 sec # 3rd Person 19 sec 
from numpy import random 
x = random.exponential(scale=2, size=(2, 3)) 
x = random.exponential(size=10) 
print(x) 

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()