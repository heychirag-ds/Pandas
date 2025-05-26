import pandas as pd 

# Read the CSV file
df = pd.read_csv("MOCK_DATA.csv")

print("Convert column data types: \n")

# Convert the "Age" column to integers with error handling
try:
    df["age"] = df["age"].astype(float)
    print(df["age"])
except ValueError as e:
    print("Error converting 'Age' column to integer:", e)
