from student import Student
from student_list import StudentList
from file_manager import FileManager


def main():
    group = StudentList()

    filename = input("Enter CSV filename: ")
    try:
        group.students = FileManager.load_from_csv(filename)
        print("Data loaded.")
    except FileNotFoundError:
        print("File not found. Starting with empty list.")

    while True:
        action = input("\n[C]reate [U]pdate [D]elete [P]rint [X]exit: ").lower()

        if action == "c":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            city = input("City: ")
            group.add_student(Student(name, phone, email, city))

        elif action == "u":
            name = input("Name to update: ")
            phone = input("New phone (or Enter): ")
            email = input("New email (or Enter): ")
            city = input("New city (or Enter): ")
            group.update_student(name, phone or None, email or None, city or None)

        elif action == "d":
            name = input("Name to delete: ")
            group.delete_student(name)

        elif action == "p":
            for s in group.get_all():
                print(s)

        elif action == "x":
            FileManager.save_to_csv("students_out.csv", group.get_all())
            print("Data saved. Exit.")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
