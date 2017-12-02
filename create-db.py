import sqlite3 as lite
import sys

con = lite.connect('data\\todo.dat')

print ("creating database/table...")

with con:
    cur = con.cursor()
    # DROP TABLE
    #cur.execute("DROP TABLE IF EXIST todo")

    # CREATE TABLES
    cur.execute("CREATE TABLE todo  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, desc TEXT, datetime TEXT)")

con.close()
print ("Database/table created.")