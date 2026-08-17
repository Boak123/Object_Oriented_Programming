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

    def __init__(self, name, university):
        self.name = name
        self.university = university

    def introduce(self):
        print(f"I am {self.name}")

    def describe(self):
        print(f"I am in {self.university}")

# Three-Level Override

class Student(Person):
    def __init__(self, name, university, course, undergraduate, student_id):
        super().__init__(name, university) # Overide + Super()
        self.student_id = student_id
        self.course = course
        self.undergraduate = undergraduate

    def describe(self):
        print(f"I am studying {self.course}")

    def introduce(self):
        print(f"I am {self.name} and student ID of {self.student_id}")

class UnderGraduateStudent(Student):
    def describe(self):
        print(f"I am in {self.undergraduate}")
        print

persongg = Person("BOLU", "Kwwasu")
persongg.introduce()
studentrr = Student("Bolu", "Kwasu", "Cyber Security", "100", 1234)
studentrr.introduce()
studentrr.describe()
undergraduate1 = UnderGraduateStudent("Victor", "Kwasu", "Cyber Security", "200", 1234)


