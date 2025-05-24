import pandas as pd 

df = pd.read_excel("data.xlsx")
print("Excel Data: ")
print(df)

df2 = pd.read_csv("data.csv")
print("")
print("CSV Data: ")
print(df2)

df3 = pd.read_json("data.json")
print("")
print("Json Data: ")
print(df3)

df4 = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
print("")
print("URL CSV Data: ")
print(df4)