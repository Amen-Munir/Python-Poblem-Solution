import pandas as pd 
import numpy as np
import matplotlib.pylab as plt 
import seaborn as sns
plt.style.use("ggplot")
pd.set_option('display.max_columns', 200)

df=pd.read_csv("CsvFiles/us-counties.csv")
# just looking at the data and its rows and columns and understanding data 

print(df.shape)
print(df.columns)
print(df)
print (df.describe())


#data preperations 

df['date']=pd.to_datetime(df['date'])
print(df.dtypes)
state_counts = df['state'].value_counts().head(10)
state_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Most Frequent states with cases')
plt.xlabel('State')
plt.ylabel('Frequency')
plt.show()
print(df.isna().sum()) #checking to see if we have null values in our data set 

state_counts = df['state'].value_counts().head(10)
state_counts.plot(kind='kde', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Most Frequent states with cases')
plt.xlabel('State')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(df['state'], df['fips'], alpha=0.5)
plt.title('Scatter Plot of State vs FIPS')
plt.xlabel('State')
plt.ylabel('FIPS')
plt.show()