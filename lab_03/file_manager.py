import csv
from student import Student


class FileManager:
    @staticmethod
    def load_from_csv(filename):
        students = []
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(
                    Student(
                        row["name"],
                        row["phone"],
                        row["email"],
                        row["city"]
                    )
                )
        return students

    @staticmethod
    def save_to_csv(filename, students):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email", "city"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow({
                    "name": s.name,
                    "phone": s.phone,
                    "email": s.email,
                    "city": s.city
                })
