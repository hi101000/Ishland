import sqlite3

conn = sqlite3.connect('users.db')

conn.execute("DROP table users")

conn.execute('''CREATE TABLE USERS
         (ID INT PRIMARY KEY     NOT NULL,
         PSSWD          TEXT    NOT NULL,
         EMAIL          TEXT    NOT NULL,
         NAME           TEXT    NOT NULL,
         DOB            INT     NOT NULL,
         POSITION       TEXT);''')
print("table created successfully!")

conn.commit()

conn.close()