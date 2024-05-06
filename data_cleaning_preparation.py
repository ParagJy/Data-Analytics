import pandas as pd

trxn= pd.read_csv(r'C:/ProgramData/MySQL/MySQL Server 5.6/Uploads/Retail_Data_Transactions.csv')
# print(trxn)

response=pd.read_csv(r'C:/ProgramData/MySQL/MySQL Server 5.6/Uploads/Retail_Data_Response.csv')
# print(response)

df=trxn.merge(response, on='customer_id',how='left')
# print(df)

# FEATURES...........

# print(df.dtypes)
# print(df.shape)
# print(df.head())          # first 5 rows
# print(df.tail())          # last 5 rows

# MISSING VALUES

# print(df.isnull().sum())

# print(df.dropna())

# change dtypes
df['trans_date']= pd.to_datetime(df['trans_date'])
df['response']= df['response'].astype('int64')            #have to fix this part
# set(df['response'])
print(df)


# print(df.dtypes)

# check for outliers
#Z-SCORE
from scipy import stats
import numpy as np

#calc z score
z_scores= np.abs(stats.zscore(df['tran_amount']))

#set a threshold

threshold= 3
outliers= z_scores>threshold
# print(df[outliers])

#calc z score
z_scores= np.abs(stats.zscore(df['response']))

#set a threshold

threshold= 3
outliers= z_scores>threshold
# print(df[outliers])

# VISUAL REPRESENTATION OF OUTLIERS............
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=df['response'])
# plt.show()

# creating new columns

# df['month']= df['trans_date'].dt.month
# print(df)