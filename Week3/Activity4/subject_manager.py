from database import create_connection
import sqlite3

def add_subjects(code, name, udsc):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (subject_code, subject_name, subject_udsc) VALUES (?, ?, ?)", (code, name, udsc))
        conn.commit()
        print(" Subject added successfully.")
    except sqlite3.IntegrityError:
        print(" Subject code must be unique.")
    conn.close()

def view_subjects():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_subject(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects WHERE subject_name LIKE ?", ('%' + name + '%' ,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_subject(subject_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subjects WHERE id = ?", (subject_id,))
    conn.commit()
    conn.close()
    print("🗑️ Subject deleted.")
