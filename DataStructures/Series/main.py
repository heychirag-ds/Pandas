import pandas as pd 

struc = pd.Series([10,20,30,40,50])
print(struc)
print(type(struc))

struc_new = pd.Series([60,70,80,90,100], index=["Josh", "Hardik", "Shreyas", "Rajat", "Jassi"])
print(struc_new)
print("Hardik's Score: ", struc_new["Hardik"])