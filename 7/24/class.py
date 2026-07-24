import pandas as pd
ages=pd.Series([25, 30, 35, 40, 45])
data={
    "names": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "ages": [25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)
print(df)

df=pd.read_csv("data.csv")
df=pd.read_json("data.json")
df=pd.read_excel("data.xlsx")

df[df["ages"] > 30]