from file_manager import FileManager
from student import Student


def test_save_and_load(tmp_path):
    file = tmp_path / "test.csv"
    students = [Student("Bob", "222", "b@mail.com", "Odesa")]

    FileManager.save_to_csv(file, students)
    loaded = FileManager.load_from_csv(file)

    assert len(loaded) == 1
    assert loaded[0].name == "Bob"
