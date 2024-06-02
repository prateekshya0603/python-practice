class Student:

    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def display_details(self):
        print("Name of the student:", self.name, self.age, self.roll)


Student1 = Student("Prateekshya", 24, 100034)
print(Student1.display_details())

Student2 = Student("Prayush", 23, 3099765)
print(Student2.name)

Student1.gender = "F"
print(Student1.gender)

Student1.age = 27
print(Student1.age)

print(Student1.display_details())
print(Student2.age)
print(getattr(Student2, "age"))
print(setattr(Student1, "age", 30))
print(getattr(Student1, "age"))

