import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Multiple line plot..........
# data={'year':[2001,2002,2003,2004,2005],
#       'sales1':[100,110,120,140,150]}
    #   'sales2':[101,160,130,125,155]}

#df=pd.DataFrame(data)

# plt.plot(df['year'],df['sales1'],label='Sales_1')
# plt.plot(df['year'],df['sales2'],label='Sales_2')
# plt.xlabel('year')
# plt.ylabel('Sales')
# plt.title("Sales over the years")
# plt.legend()
# plt.show()

# Bar line plot..........
# plt.bar(df['year'],df['sales1'])
# plt.xlabel('year')
# plt.ylabel('Sales')
# plt.title("Sales by year")
# plt.show()

# Scatter plot with trend line.......
# sns.regplot(x='year',y='sales1',data=df)
# plt.xlabel=('X')
# plt.ylabel=('Y')
# plt.title("Scatter plot with trend line")
# plt.show()

# HISTOGRAM...............
# np.random.seed(42)
# data=np.random.normal(loc=50,scale=10,size=1000)
# df=pd.DataFrame({'values':data})
# # print(df)
# plt.hist(df['values'],bins=20,color='purple',edgecolor='yellow')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title("HISTOGRAM")
# plt.show()

# BOX PLOT........
# data={'category':['A','A','A','B','B','B'],
#       'value':[10,15,20,25,30,35]}

# df=pd.DataFrame(data)
# sns.boxplot(x='category',y='value',data=df)
# plt.xlabel('Category')
# plt.ylabel('Values')
# plt.title("BOX PLOT")
# plt.show()

# HEATMAP..
data={'A':[1,2,3],
      'B':[4,5,6],
      'C':[7,8,9]}

df=pd.DataFrame(data)
sns.heatmap(df,annot=True,cmap='crest')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.title("HEATMAP")
plt.show()