import sqlite3

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT name, age, score 
    FROM games 
    JOIN users ON games.user_id = users.id
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
