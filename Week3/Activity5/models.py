from database import Database
import sqlite3

class Customer:
    def __init__(self):
        database = Database()
        self.conn = database.create_connection()
        

    def create_customer(self, name, email, phone):
        cursor = self.conn.cursor()
        
        try:
            cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            self.conn.commit()
            customer_id = cursor.lastrowid
            print("Customer created successfully with ID: ", customer_id)
        except sqlite3.IntegrityError:
            print(" Email and phone must be unique.")
        self.conn.close()

    def view_customers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        self.conn.close()
        return rows    
    

class Currency:
    def __init__(self):
        database = Database()
        self.conn = database.create_connection()
        

    def create_currency(self, code, name, exchange_rate):
        cursor = self.conn.cursor()
        
        try:
            cursor.execute("INSERT INTO currencies (code, name, exchange_rate) VALUES (?, ?, ?)", (code, name, exchange_rate))
            self.conn.commit()
            print("Currency created successfully.")
        except sqlite3.IntegrityError:
            print(" Currency code must be unique.")
        self.conn.close()

    def view_currencies(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM currencies")
        rows = cursor.fetchall()
        self.conn.close()
        return rows

    def view_currency_by_code(self, code):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM currencies WHERE code = ?", (code,))
        rows = cursor.fetchall()
        self.conn.close()
        return rows    
    

class CurrencyExchange():
    def __init__(self):
        database = Database()
        self.conn = database.create_connection()
        

    def create_currency_exchange(self, customer_id, from_currency_code, to_currency_code, original_amount, converted_amount):
        cursor = self.conn.cursor()
        
        try:
            cursor.execute("INSERT INTO currency_exchange (customer_id, from_currency_code, to_currency_code, original_amount, converted_amount) VALUES (?, ?, ?, ?, ?)", (customer_id, from_currency_code, to_currency_code, original_amount, converted_amount))
            self.conn.commit()
            print("Currency exchange created successfully.")
        except sqlite3.IntegrityError:
            print("Id must be unique.")
        self.conn.close()

    def view_currency_exchange(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM currency_exchange")
        rows = cursor.fetchall()
        self.conn.close()
        return rows