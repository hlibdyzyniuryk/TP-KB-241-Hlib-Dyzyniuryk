students = [
    {"name": "Olena", "grade": 88},
    {"name": "Andriy", "grade": 75},
    {"name": "Maria", "grade": 95},
    {"name": "Ivan", "grade": 82}
]

sorted_by_name = sorted(students, key=lambda student: student["name"])
print("Sorted by name:")
print(sorted_by_name)

sorted_by_grade = sorted(students, key=lambda student: student["grade"])
print("\nSorted by grade:")
print(sorted_by_grade)

sorted_by_grade_desc = sorted(
    students,
    key=lambda student: student["grade"],
    reverse=True
)
print("\nSorted by grade (descending):")
print(sorted_by_grade_desc)
