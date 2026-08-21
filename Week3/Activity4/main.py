# Queries for creating database and tables
from database import create_tables
# Functions and SQL queries for Students table CRUD
from student_manager import add_students, view_students, search_student, delete_student
# Functions and SQL queries for Subjects table CRUD
from subject_manager import add_subjects, view_subjects, search_subject, delete_subject
# Functions SQL queries for Lectures table CRUD
from lecturer_manager import add_lecturers, view_lecturers, search_lecturer, delete_lecturer
# Functions SQL queries for Enrollments table CRUD
from enrollment_manager import add_enrollment, view_enrollments, search_enrollment, delete_enrollment
# Functions SQL queries for Lectures table CRUD
from lecture_manager import add_lecture, view_lectures, search_lecture, delete_lecture

def menu():
    # Menu items for Students
    print("\n==== Students Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Delete Student by ID")

    # Menu items for Subjects (Courses)
    print("\n==== Subjects(Courses) Manager ====")
    print("5. Add Subject")
    print("6. View All Subject")
    print("7. Search Subject by Name")
    print("8. Delete Subject by ID")

    # Menu items for Lecturers
    print("\n==== Lecturers Manager ====")
    print("9. Add Lecturer")
    print("10. View All Lecturers")
    print("11. Search Lecturer by Name")
    print("12. Delete Lecturer by ID")

    # Menu items for Enrollments
    print("\n==== Enrollments Manager ====")
    print("13. Add Enrollment")
    print("14. View All Enrollments")
    print("15. Search Enrollment by Student Name")
    print("16. Search Enrollment by Subject Name")
    print("17. Delete Enrollment by ID")

    # Menu items for Lectures
    print("\n==== Lectures Manager ====")
    print("18. Add Lecture")
    print("19. View All Lectures")
    print("20. Search Lecture by Lecturer Name")
    print("21. Search Lecture by Subject Name")
    print("22. Delete Lecture by ID")

    # Menu for Exit
    print("99. Exit")

def main():
    create_tables()
    menu()
    while True:
        choice = input("Select an option: ")
        
        if choice == '1': # Create Student
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            birth_date = input("Enter birth date: ")
            email = input("Enter email: ")
            add_students(f_name, l_name, birth_date, email)
        elif choice == '2': # View Students
            users = view_students()
            for user in users:
                print(user)
        elif choice == '3': # Search Student
            name = input("Enter name to search: ")
            students = search_student(name)
            for student in students:
                print(student)
        elif choice == '4': # Delete Student
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)


        elif choice == '5': # Create Subject
            s_code = input("Enter subject code: ")
            s_name = input("Enter subject name: ")
            s_udsc = input("Enter udsc: ")
            add_subjects(s_code, s_name, s_udsc)
        elif choice == '6': # View Subject
            subjects = view_subjects()
            for subject in subjects:
                print(subject)
        elif choice == '7': # Search Subject
            name = input("Enter subject name to search: ")
            subjects = search_subject(name)
            for subject in subjects:
                print(subject)
        elif choice == '8': # Create Subject
            subject_id = int(input("Enter subject ID to delete: "))
            delete_subject(subject_id)


        elif choice == '9': # Create Lecturer
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            add_lecturers(f_name, l_name, address, email)
        elif choice == '10': # View Lecturer
            lecturers = view_lecturers()
            for lecturer in lecturers:
                print(lecturer)
        elif choice == '11': # Search Lecturer
            name = input("Enter lecturer name to search: ")
            lecturers = search_lecturer(name)
            for lecturer in lecturers:
                print(lecturer)
        elif choice == '12': # Delete Lecturer
            lecturer_id = int(input("Enter lecturer ID to delete: "))
            delete_lecturer(lecturer_id)


        elif choice == '99': # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
