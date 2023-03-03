import sqlite3
import re


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as error:
        print(error)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def create_product(conn, product: tuple):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def update_quantity(conn, product: tuple):
    try:
        sql = '''update products set quantity = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def update_price(conn, product: tuple):
    try:
        sql = '''update products set price = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def select_all_products(conn):
    try:
        sql = '''select * from products
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_by_price_and_quantity(conn, limit):
    try:
        sql = '''select * from products where price < ? and quantity > ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def search_by_word(conn, word):
    try:
        sql = '''select * from products where product_title like ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


database = r'hw8.db'

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price  DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''

connection = create_connection(database)
create_table(connection, sql_create_products_table)
create_product(connection, ('Мыло', 60.7, 110))
create_product(connection, ('Мыло детское', 70.1, 90))
create_product(connection, ('Хозяйственное мыло', 40.94, 100))
create_product(connection, ('Масло сливочное', 120.2, 180))
create_product(connection, ('Подсолнечное масло', 150.99, 200))
create_product(connection, ('Арахисовая паста', 150.99, 67))
create_product(connection, ('Зубная паста', 250.17, 250))
create_product(connection, ('Хлеб пшеничный', 25.9, 450))
create_product(connection, ('Ржаной хлеб', 30.9, 300))
create_product(connection, ('Сухарики', 60.99, 240))
create_product(connection, ('Жвачка мятная', 30.9, 370))
create_product(connection, ('Жвачка арбузная', 34.9, 360))
create_product(connection, ('Лепешка', 35.0, 450))
create_product(connection, ('Дневник', 100.99, 60))
create_product(connection, ('Ежедневник', 350.99, 35))
update_quantity(connection, (450, 250))
update_price(connection, (150.99, 149.99))
delete_product(connection, 3)
select_all_products(connection)
select_by_price_and_quantity(connection, (100, 5))
search_by_word(connection, 'дневник')

connection.close()