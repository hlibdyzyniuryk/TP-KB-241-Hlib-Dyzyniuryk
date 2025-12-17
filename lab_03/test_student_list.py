from student import Student
from student_list import StudentList


def test_add_student():
    group = StudentList()
    group.add_student(Student("Anna", "123", "a@mail.com", "Kyiv"))
    assert len(group.students) == 1


def test_delete_student():
    group = StudentList()
    group.add_student(Student("Tom", "111", "t@mail.com", "Lviv"))
    group.delete_student("Tom")
    assert len(group.students) == 0
