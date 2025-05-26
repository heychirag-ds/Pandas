import pandas as pd

df = pd.read_csv("MOCK_DATA.csv")

#Lambda Function
try:
    df["age_group"] = df["Age"].apply(lambda x:  "Adult" if x >= 18 else "Minor")
    print(df["age_group"])
except Exception as e:
    print("Error: ", e)
    
#Element wise map for series
gender_map = {"M": "Male", "F": "Female"}
print(df["gender"].map(gender_map))

print(df["country"].replace({"Aus": "Australia", "Ind": "India"}))