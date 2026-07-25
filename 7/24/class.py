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



import sqlite3
conn=sqlite3.connect("data.db")
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
cursor.execute("INSERT INTO users (name, age) VALUES ('David', 40)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Eve', 45)")
conn.commit()


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()

