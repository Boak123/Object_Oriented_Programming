class Person:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Student(Person):
    pass

student1 = Student()
student1.eat()