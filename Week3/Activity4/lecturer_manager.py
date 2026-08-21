from database import create_connection
import sqlite3

def add_lecturers(f_name, l_name, address, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturers (l_first_name, l_last_name, l_address, l_email) VALUES (?, ?, ?, ?)", (f_name, l_name, address, email))
        conn.commit()
        print(" Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_lecturer(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturers WHERE l_first_name LIKE ? OR l_last_name LIKE ?", ('%' + name + '%', '%' + name + '%', ))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_lecturer(lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lecturer WHERE id = ?", (lecturer_id,))
    conn.commit()
    conn.close()
    print("🗑️ Lecturer deleted.")
