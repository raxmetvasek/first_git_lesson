import sqlite3

def create_tbl():
    conn=sqlite3.connect("university.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER  PRIMARY KEY, 
        name TEXT,
        mark REAL,
        age INTEGER)""")
    conn.commit()
    conn.close()


def insert_into():
    conn=sqlite3.connect("university.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO students(name, mark, age) VALUES ('Osokin', 4.2, 19)")
    conn.commit()
    conn.close()

#create_tbl()
#insert_into()

def update_info(id, age):
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET age = ? WHERE id = ?", 
        (age, id)
    )
    
    #Фиксируем изменения в базе данных и закрываем
    conn.commit()
    conn.close()
    print(f"Данные студента с ID {id} успешно обновлены!")




update_info(1, 25)

def rm_info(id, age):
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    cursor.execute(
        "REMOVE students SET age = ? WHERE id = ?", 
        (age, id)
    )
    
    #Фиксируем изменения в базе данных и закрываем соединение
    conn.commit()
    conn.close()
    print(f"Данные студента с ID {id} успешно обновлены!")
    
create_tbl()
insert_into()
