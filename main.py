import sqlite3

class db:
    def __init__(self):
        self.database = sqlite3.connect("database.db")
        self.cursor = self.database.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                phone_numbers TEXT,
                rank TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nameProducts UNIQUE,
                price INTEGER
            )
        """)
    # Users
    def insert_users(self, name, address, phone_numbers, rank = 'member'):
        self.cursor.execute("""
            INSERT INTO Users(name, address, phone_numbers, rank)
            VALUES('{}', '{}', '{}', '{}');
        """.format(name, address, phone_numbers, rank))
        self.database.commit()
    def print_table_users(self):
        self.cursor.execute("SELECT * FROM Users")
        rows = self.cursor.fetchall()
        print('ĐỊNH DẠNG: ID | NAME | ADDRESS | PHONE NUMBERS | RANK')
        for row in rows: 
            print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}')
    # def delete_users(self, id):
    #     self.cursor.execute("""
    #         DELETE FROM Users
    #         WHERE id = {}
    #     """.format(id))
    #     self.database.commit()
    def count_users(self):
        self.cursor.execute("SELECT COUNT(*) FROM Users")
        count = self.cursor.fetchone()[0]
        print(count)
    # Products
    def add_product(self, name_product, price):
        self.cursor.execute("""
            INSERT INTO Products(nameProducts, price)
            VALUES('{}', {})
        """.format(name_product, price))
        self.database.commit()
    def print_table_products(self):
        self.cursor.execute("SELECT * FROM Products")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}k")
    def count_products(self):
        self.cursor.execute("SELECT COUNT(*) FROM Products")
        count = self.cursor.fetchone()[0]
        print(count)
    def delete_product(self, id):
        self.cursor.execute("""
            DELETE FROM Products
            WHERE id = {}
        """.format(id))
        self.database.commit()
    def edit_price_products(self, id, price_new):
        self.cursor.execute("""
            UPDATE Products
            SET price = {}
            WHERE id = {}
        """.format(price_new, id))
        self.database.commit()
data = db()
data.cursor.execute("SELECT * FROM Users")
dulieu = data.cursor.fetchall()
print(dulieu)