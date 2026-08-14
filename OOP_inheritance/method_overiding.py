# # Overiding

# class Person:
#     def introduce(self):
#         print("I am a Person")

# class Student(Person):
#     def introduce(self):
#         print("I am a student")

# class Lecturer(Person):
#     def introduce(self):
#         print("I am a Lecturer")

# class Administrator(Person):
#     def introduce(self):
#         print("I am an Administrator")


# person1 = Person()
# person1.introduce()
# student1 = Student()
# student1.introduce()
# lecturer1 = Lecturer()
# lecturer1.introduce()
# administrator1 = Administrator()
# administrator1.introduce()

# Overiding with attributes

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def introduce(self):
        print(f"I am {self.name} and student ID of {self.student_id}")

persongg = Person("BOLU")
persongg.introduce()
studentrr = Student("Bolu", 1234)
studentrr.introduce()

