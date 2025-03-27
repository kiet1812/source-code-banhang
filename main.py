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
                phone_numbers TEXT
            )
        """)
    def insert_users(self, name, address, phone_numbers):
        self.cursor.execute("""
            INSERT INTO Users(name, address, phone_numbers)
            VALUE('{}', '{}', '{}')
        """.format(name, address, phone_numbers))

data = db()