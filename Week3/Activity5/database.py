import sqlite3

class Database:

    def create_connection(self):
        conn = sqlite3.connect("currency_exchange.db")
        return conn


    def create_tables(self):
        conn = self.create_connection()
        cursor = conn.cursor()

        # Create students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone DATE NOT NULL UNIQUE
            )
        ''')

        # Create subjects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS currencies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                exchange_rate DOUBLE NOT NULL
            )
        ''')

        # Create lecturers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS currency_exchange (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                from_currency_code TEXT NOT NULL,
                to_currency_code TEXT NOT NULL,
                original_amount DOUBLE NOT NULL,
                converted_amount DOUBLE NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
