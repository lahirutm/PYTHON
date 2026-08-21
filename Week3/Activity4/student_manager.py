from database import create_connection
import sqlite3

def add_students(f_name, l_name, birth_date, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (f_name, l_name, birth_date, email) VALUES (?, ?, ?, ?)", (f_name, l_name, birth_date, email))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE l_name LIKE ? OR f_name LIKE ?", ('%' + name + '%', '%' + name + '%', ))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")
