import sqlite3 as sql

conn = sql.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        password VARCHAR(50) NOT NULL
    )
""")

print("Table created.")

conn.close()

