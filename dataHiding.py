class Student:
    __percentage = 0
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_percentage(self):