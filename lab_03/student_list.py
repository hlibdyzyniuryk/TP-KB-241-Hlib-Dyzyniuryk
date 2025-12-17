from student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
        self.students.sort(key=lambda s: s.name)

    def delete_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, phone=None, email=None, city=None):
        for s in self.students:
            if s.name == name:
                if phone:
                    s.phone = phone
                if email:
                    s.email = email
                if city:
                    s.city = city
                return True
        return False

    def get_all(self):
        return self.students
