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
    def insert_users(self, name, address, phone_numbers, rank = 'member'):
        self.cursor.execute("""
            INSERT INTO Users(name, address, phone_numbers, rank)
            VALUES('{}', '{}', '{}', '{}');
        """.format(name, address, phone_numbers, rank))
        self.database.commit()
    def print_table(self):
        self.cursor.execute("SELECT * FROM Users")
        rows = self.cursor.fetchall()
        print('ĐỊNH DẠNG: ID | NAME | ADDRESS | PHONE NUMBERS | RANK')
        for row in rows: 
            print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}')
    def delete_users(self, id):
        self.cursor.execute("""
            DELETE FROM Users
            WHERE id = {}
        """.format(id))
        self.database.commit()
    def count_users(self):
        self.cursor.execute("SELECT COUNT(*) FROM Users")
        count = self.cursor.fetchone()
        print(count[0])


data = db()
# data.insert_users('Pham Tuan Kiet', '755 - Dong Tai - Van Thang - Nong Cong - Thanh Hoa', '0396138606', 'Chu quan')
# data.delete_users(1)
# data.print_table()
data.count_users()