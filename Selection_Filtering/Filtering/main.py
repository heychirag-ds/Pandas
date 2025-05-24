import pandas as pd 

df = pd.read_csv("new_data.csv")

df2 = df[df['IMDB'] < 7]
print("Films with IMDB less than 7: ", df2)

df3 = df[(df['IMDB'] < 7) & (df['Collection'] > '100 cr')]
print(df3)

df4 = df.query("IMDB < 8 and Genre == 'Drama'")
print(df4)