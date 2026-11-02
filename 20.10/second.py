import sqlite3

conn = sqlite3.connect('my_database1.db') 
from contextlib import closing
with closing (sqlite3 connect("database.db")) as conn:
    with conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO")
        
cursor.execute("SELECT id,")
rows=cursor.fetchall()
users=[]
for row in rows:
    users.append(row[1])
    
conn.row_factory=sqlite3.Row
cursor=conn.cursor()
cursor.execute("SELECT id, name, email FROM users")
for row in cursor.fetchall():
    print(row['name'], row['email'])
