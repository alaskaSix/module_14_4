import sqlite3

connection = sqlite3.connect('Production.dp')
cursor = connection.cursor()

# Подготовительный код

#cursor.execute("DELETE FROM Products")
#for num in range(1, 5):
#    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                (f"Продукт {num}", f"Описание {num}", num * 100))
#connection.commit()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
        ''')
    connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()




