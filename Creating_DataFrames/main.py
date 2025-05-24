import pandas as pd 
import numpy as np

data = [
    ["Hardik", "MI"],
    ["Shreyas", "PBKS"],
    ["Rishabh", "LSG"]
]

df = pd.DataFrame(data, columns=["Name", "Team"])
print(df)

arr = np.array([[1,2], [3,4]])
df2 = pd.DataFrame(arr, columns=["A", "B"])
print(df2)