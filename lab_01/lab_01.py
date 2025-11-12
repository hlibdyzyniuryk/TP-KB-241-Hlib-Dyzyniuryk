students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "city": "Kyiv"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "city": "Lviv"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@gmail.com",  "city": "Kharkiv"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@gmail.com",  "city": "Odesa"}
]


def print_all():
    print("\n=== Current list of students ===")
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, City: {elem['city']}")
    print("=================================\n")


def add_new():
    name = input("Enter student's name: ")
    phone = input("Enter student's phone: ")
    email = input("Enter student's email: ")
    city = input("Enter student's city: ")
    new_item = {"name": name, "phone": phone, "email": email, "city": city}

    insert_position = 0
    for item in students:
        if name > item["name"]:
            insert_position += 1
        else:
            break
    students.insert(insert_position, new_item)
    print("New student added.\n")


def delete_student():
    name = input("Enter the student's name to delete: ")
    delete_position = -1
    for item in students:
        if name == item["name"]:
            delete_position = students.index(item)
            break
    if delete_position == -1:
        print("Student not found.\n")
    else:
        del students[delete_position]
        print("Student deleted successfully.\n")


def update_student():
    name = input("Enter the student's name to update: ")
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break

    if not found:
        print("Student not found.\n")
        return

    print(f"Current data: {found}")
    print("Leave a field empty to keep the current value.")

    new_name = input(f"New name ({found['name']}): ") or found['name']
    new_phone = input(f"New phone ({found['phone']}): ") or found['phone']
    new_email = input(f"New email ({found['email']}): ") or found['email']
    new_city = input(f"New city ({found['city']}): ") or found['city']

    found.update({"name": new_name, "phone": new_phone, "email": new_email, "city": new_city})

    students.sort(key=lambda x: x["name"])
    print("Student data updated.\n")


def main():
    while True:
        choice = input("Choose action [C - Create, U - Update, D - Delete, P - Print, X - Exit]: ").lower()
        match choice:
            case "c":
                add_new()
                print_all()
            case "u":
                update_student()
                print_all()
            case "d":
                delete_student()
                print_all()
            case "p":
                print_all()
            case "x":
                print("Exiting the program.")
                break
            case _:
                print("Unknown command, please try again.")


if __name__ == "__main__":
    main()
