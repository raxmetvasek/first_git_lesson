import sqlite3

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS games (user_id INTEGER, score INTEGER)")
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM games")

cursor.execute("INSERT INTO users VALUES (1, 'Kolya', 20)")
cursor.execute("INSERT INTO users VALUES (2, 'Petya', 21)")
cursor.execute("INSERT INTO users VALUES (3, 'Ivan', 20)")
cursor.execute("INSERT INTO users VALUES (4, 'Nikolay', 22)")
cursor.execute("INSERT INTO users VALUES (5, 'Sergey', 19)")

cursor.execute("INSERT INTO games VALUES (4, 100500)")
cursor.execute("INSERT INTO games VALUES (2, 1000)")
cursor.execute("INSERT INTO games VALUES (5, 5000)")
cursor.execute("INSERT INTO games VALUES (3, 10000)")

conn.commit()
conn.close()

print("Файл accounts.db успешно создан и заполнен!")
