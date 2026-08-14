class Person:
    def introduce(self):
        print("I am a Person")

class Student(Person):
    def introduce(self):
        print("I am a student")

class Lecturer(Person):
    def introduce(self):
        print("I am a Lecturer")

class Administrator(Person):
    def introduce(self):
        print("I am an Administrator")

student1 = Student()
student1.introduce()