import sqlite3

conn = sqlite3.connect('my_database.db', timeout= 5.0) 
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance INTEGER NOT NULL
)
""")
conn.commit()

cursor.execute("DELETE FROM accounts")

cursor.execute("INSERT INTO accounts (id, name, balance) VALUES (1, 'Kolya', 1500)")
cursor.execute("INSERT INTO accounts (id, name, balance) VALUES (2, 'Petya', 2500)")
conn.commit()

print("Данные до перевода:")
cursor.execute("SELECT * FROM accounts")
print(cursor.fetchall()) 


try:
    cursor.execute("UPDATE accounts SET balance= balance -1000 WHERE id =1")
    cursor.execute("UPDATE accounts SET balance= balance +1000 WHERE id=2")
    conn.commit()
    print("\nДеньги переведены")
except:
    conn.rollback()
    
    
print("\nДанные после перевода")
cursor.execute("SELECT * FROM accounts")
print(cursor.fetchall())

conn.close()
