import pandas as pd 

df = pd.read_csv("data_cleaning.csv")

print("Data in CSV file: \n", df)

print()

print(df.isnull()) #Displays where null value is true or false
print()
print(df.isnull().sum()) #Gives total sum of null values in each column
print()
print(df.dropna()) #Prints only columns with values
print()
print(df.dropna(axis=1)) #Drops columns with null values
print()
print(df.fillna(0)) #Fills columns with null values
print()
print(df['Age'].fillna(df['Age'].mean())) #Fills null values with average
print()
print(df.fillna(method="bfill"))