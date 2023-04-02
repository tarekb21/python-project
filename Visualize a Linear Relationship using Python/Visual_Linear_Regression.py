import pandas as pd  #clean messy data sets, and make them readable and relevant data
import numpy as np  #work for arrays 
import matplotlib.pyplot as plt 
import seaborn as sns 



#The dropna() method removes the rows that contains NULL values
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding = 'latin1')
data = data.dropna()
print(data.head())

#visualize 
#The regplot function generates a scatter plot with a regression line.
y = data['Likes']
x1 = data['Impressions']

plt.scatter(x1,y)
plt.xlabel('Impressions',fontsize = 20)
plt.ylabel('Likes',fontsize = 20)
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()


