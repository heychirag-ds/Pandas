import pandas as pd

df = pd.read_csv("data_cleaning.csv")

print("CSV Data: \n", df)
print()
print("Duplicate Data: \n", df.duplicated())
print()
print("CSV without duplicates: \n", df.drop_duplicates())
print()
print("Check two cols: \n", df.duplicated(subset=["Name", "Age"]))