import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
print("")
print("First 5 rows:")
print(df.head())

print("")
print("Last 5 rows:")
print(df.tail())

print("")
print("Dataset Information:")
print(df.info())

print("")
print("Statistical Parameters:")
print(df.describe())

print("")
print("Columns:")
print(df.columns)

print("")
print("Shape:")
print(df.shape)