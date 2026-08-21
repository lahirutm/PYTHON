import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            birth_date DATE NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Create subjects table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_code TEXT NOT NULL UNIQUE,
            subject_name TEXT NOT NULL,
            subject_udsc TEXT NOT NULL
        )
    ''')

    # Create lecturers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            l_first_name TEXT NOT NULL,
            l_last_name TEXT NOT NULL,
            l_email TEXT NOT NULL UNIQUE,
            l_address TEXT NOT NULL
        )
    ''')

    # Create enrollments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL
        )
    ''')

    # Create lectures table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecturer_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            l_date DATE NOT NULL,
            l_time TIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
