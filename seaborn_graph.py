import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 

# create histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=True)
plt.show()

# Plotting a Distplot Without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

# creating graph using  file
x = pd.read_csv("googleplaystore.csv") 
sns.distplot(x.Rating) 
plt.show() 

# adding color
sns.distplot(x.Rating,bins=20,kde=False,color='g') 
plt.title("Distribution Graph",fontsize=40,color='red') 
plt.show() 

# adding background
plt.style.use("dark_background") 
sns.distplot(x.Rating,bins=20,kde=False,color='g')
plt.title("Distribution Graph",fontsize=40,color='red') 
plt.show() 


# pie chart
x['Content Rating'].value_counts() 
x['Content Rating'].value_counts().plot.pie() 
plt.show() 

# bar chart
x['Content Rating'].value_counts().plot.bar() 
plt.show()