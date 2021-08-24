# Step 1 Load the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 2 Read in the Boston housing dataset (given as a csv file) from the local directory
nRowRead = None
df = pd.read_csv('HousingData.csv', delimiter=',', nrows=nRowRead)
nRow, nCol = df.shape
print (f'There are {nRow} rows and {nCol} columns')

# Step 3 Check the first 10 records Find the total number of records
print(df.head(10))

# Step 4 Create a smaller DataFrame with columns that do not include CHAS, NOX, B, and LSTAT
df1 = df.drop(['CHAS','NOX','B','LSTAT'], axis=1)
print (df1)

#Step 5 Check the last seven records of the new DataFrame you just created
print (df1.tail(7))

# Step 6 Plot the histograms of all the variables (column) in the new DataFrame
df1.hist(figsize=(10,10), layout=(3,5))
plt.show()

# Step 7 Plot them all at once using a for loop Try to add a unique title to a plot
cols = list(df.columns)
for col in cols:
    df[col].hist(figsize=(10,10))
    plt.title(f'{col}', fontsize=16)
    plt.show()

# Step 8 Create a scatter plot of crime rate versus price
plt.figure(figsize=(8,6))
plt.title('Plot of Crime rate vs Price', fontsize=20, c='purple')
plt.xlabel('Crime rate', fontsize=16, c='purple')
plt.ylabel('Price ($)', fontsize=16, c='purple')
plt.grid(True)
plt.scatter(x=df['CRIM'], y=df['MEDV'], c='pink', s=40, edgecolors='k')
plt.show()

# Step 9 Plot using log10(crime) versus price
df['log10(crime)'] = np.log10(df['CRIM'])
plt.figure(figsize=(8,6))
plt.title('Plot of log10(crime) vs Price', fontsize=20, c='purple')
plt.xlabel('log10(crime)', fontsize=16, c='purple')
plt.ylabel('Price ($)', fontsize=16, c='purple')
plt.grid(True)
plt.scatter(x=df['log10(crime)'], y=df['MEDV'], c='pink', s=40, edgecolors='k')
plt.show()

# Option 2
plt.scatter(np.log10(df['CRIM']), df['MEDV'])


# Step 10 Calculate some useful statistics, such as mean rooms per dwelling, median age, mean distances 
# to five Boston employment centers and the percentage of houses with a low price (< $20 000)
print(f"Mean rooms per dwelling is {round(df['RM'].mean(),2)} rooms")
print(f"Median age is {round(df['AGE'].median(),2)} years old")
print(f"Mean distances to 5 Boston employment centers is {round(df['DIS'].mean(),2)} km")

low_price = df['MEDV'] < 20
pcnt = low_price.mean()*100
print(f"The percentage of houses with a low price (<$20,000) is {pcnt}%")