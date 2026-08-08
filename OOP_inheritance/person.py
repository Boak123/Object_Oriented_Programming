class Person:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Student(Person):

    def study(self):
        print("studying")

    def take_exam(self):
        print("Taking an Exam")

class Lecturer(Person):

    def Teach(self):
        print("Teaching")

class Administerator(Person):

    def Rigistra(self):
        print("Registering Student")

student1 = Student()
student1.eat()
student1.study()
student1.take_exam()