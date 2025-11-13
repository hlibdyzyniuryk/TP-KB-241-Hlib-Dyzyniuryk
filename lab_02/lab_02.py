import csv
from sys import argv

students = []

def load_from_csv(file_name):
    global students
    with open(file_name, "r", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        students = [row for row in reader]
    print("Data loaded from file.")

def save_to_csv(file_name):
    with open(file_name, "w", newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "email", "city"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    print("Data saved to file.")

def add_student():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    city = input("Enter city: ")
    students.append({"name": name, "phone": phone, "email": email, "city": city})
    students.sort(key=lambda x: x["name"])
    print("Student added.")

def delete_student():
    name = input("Enter name to delete: ")
    global students
    students = [s for s in students if s["name"] != name]
    print("Student deleted if existed.")

def update_student():
    name = input("Enter name to update: ")
    for s in students:
        if s["name"] == name:
            print(f"Current data: {s}")
            new_phone = input(f"New phone ({s['phone']}): ") or s['phone']
            new_email = input(f"New email ({s['email']}): ") or s['email']
            new_city = input(f"New city ({s['city']}): ") or s['city']
            s.update({"phone": new_phone, "email": new_email, "city": new_city})
            print("Student updated.")
            break
    else:
        print("Student not found.")

def print_all():
    for s in students:
        print(f"{s['name']:10} {s['phone']:12} {s['email']:20} {s['city']}")

def main():
    if len(argv) < 2:
        print("Please provide CSV filename as argument.")
        return
    file_name = argv[1]
    load_from_csv(file_name)

    while True:
        action = input("\n[C]reate [U]pdate [D]elete [P]rint [X]exit: ").lower()
        if action == "c":
            add_student()
        elif action == "u":
            update_student()
        elif action == "d":
            delete_student()
        elif action == "p":
            print_all()
        elif action == "x":
            save_to_csv("students_out.csv")
            print("Exiting program.")
            break
        else:
            print("Unknown action, try again.")


if __name__ == "__main__":
    main()
