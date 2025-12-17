class Student:
    def __init__(self, name, phone, email, city):
        self.name = name
        self.phone = phone
        self.email = email
        self.city = city

    def __str__(self):
        return f"{self.name:10} {self.phone:12} {self.email:20} {self.city}"
