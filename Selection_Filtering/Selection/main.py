import pandas as pd

df = pd.read_csv("data.csv")

print(df["Name"])
print(df[["Name", "Film"]])
print(df.loc[2])
print(df.loc[5, 'Genre'])
print(df.loc[3:7, ['Name', 'Film', 'Year']])
print(df.iloc[3:7, 0:2])

print(df.at[0, "Film"])