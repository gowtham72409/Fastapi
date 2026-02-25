import sqlite3

conn=sqlite3.connect("mydatabse.db")

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emp(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
               )
""")

cursor.execute("INSERT INTO emp(name,age) VALUES (?,?)", ("Gowtham",24))
cursor.execute("INSERT INTO emp(name,age) VALUES (?,?)", ("Gowsith",26))
cursor.execute("INSERT INTO emp(name,age) VALUES (?,?)", ("Rahul",25))
cursor.execute("INSERT INTO emp(name,age) VALUES (?,?)", ("Ranjith",28))
cursor.execute("INSERT INTO emp(name,age) VALUES (?,?)", ("Dhaya",25))
cursor.execute("INSERT INTO emp(name,age) VALUES (?,?)", ("Nithish",20))

conn.commit()

cursor.execute("select * from emp")
row=cursor.fetchall()

for i in row:
    print(i)