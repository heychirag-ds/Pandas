import pandas as pd 

data = {
    "Name": ["Mitchell", "Josh", "Pat"],
    "Age": [32, 30, 31],
    "Teams": ["RCB", "DC", "SRH"]
}
df = pd.DataFrame(data)
print(df)

print(df.index)

print(df.columns)