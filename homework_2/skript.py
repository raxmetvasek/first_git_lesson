import json
import sqlite3

''' Загрузка данных из JSON-файла '''
with open('catalog.json', 'r', encoding='utf-8') as file:
    products_data = json.load(file)

''' Подключение к базе данных SQLite '''
conn = sqlite3.connect('online_shop.db')
cursor = conn.cursor()

''' Включаем поддержку Foreign Keys в SQLite '''
cursor.execute("PRAGMA foreign_keys = ON;")

'''  Создание таблицы категорий '''
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
)
''')

''' Создание таблицы товаров с внешним ключом на категории '''
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE SET NULL
)
''')

''' Словарь для отслеживания существующих категорий и их ID в базе данных '''
category_mapping = {}

'''  Перенос и нормализация данных '''
for item in products_data:
    category_info = item['category']
    category_name = category_info['name']
    category_desc = category_info['description']
    
    ''' Если категория еще не была добавлена, сохраняем ее в БД '''
    if category_name not in category_mapping:
        cursor.execute('''
        INSERT OR IGNORE INTO categories (name, description)
        VALUES (?, ?)
        ''', (category_name, category_desc))
        
        ''' Получаем id созданной (или уже существовавшей) категории '''
        cursor.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
        category_id = cursor.fetchone()[0]
        category_mapping[category_name] = category_id
    else:
        category_id = category_mapping[category_name]
        
    ''' Вставка самого товара с привязкой по category_id '''
    cursor.execute('''
    INSERT INTO products (product_name, price, category_id)
    VALUES (?, ?, ?)
    ''', (item['product_name'], item['price'], category_id))

conn.commit()
conn.close()

print("Данные сохранены в result.db")
