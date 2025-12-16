class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"


students = [
    Student("Olena", 20),
    Student("Andriy", 18),
    Student("Maria", 22),
    Student("Ivan", 19)
]

sorted_students = sorted(students, key=lambda s: s.age)

for student in sorted_students:
    print(student)
