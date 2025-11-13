from lab_02 import load_from_csv, save_to_csv

def test_load_from_csv(tmp_path):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("name,phone,email,city\nAnna,123,anna@mail.com,Kyiv\n")

    load_from_csv(str(csv_file))
    assert len(__import__('lab_02').students) == 1
    assert __import__('lab_02').students[0]["name"] == "Anna"

def test_save_to_csv(tmp_path):
    csv_file = tmp_path / "output.csv"
    mod = __import__('lab_02')
    mod.students = [{"name": "Tom", "phone": "111", "email": "t@mail.com", "city": "Odesa"}]
    save_to_csv(str(csv_file))
    text = csv_file.read_text()
    assert "Tom" in text
