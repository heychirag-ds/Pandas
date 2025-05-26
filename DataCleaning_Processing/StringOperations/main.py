import pandas as pd 

df = pd.read_csv("data_cleaning.csv")

print("Convert all names to lowercase: \n")
print(df["Name"].str.lower())
print("Checks a specific condition: \n")
print()
print(df["City"].str.contains("delhi", case=False))
print("Outputs a pandas Series where each element is in a list: \n")
print()
print(df["Email"].str.split("@"))