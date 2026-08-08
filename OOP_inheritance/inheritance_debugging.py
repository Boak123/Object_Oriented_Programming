# Find the Error

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()

# Solution: you call the eat method from class without putting the (Animal) in line 9 in the dog class to inherit from it

# Find the error

class Vehicle:

    def start(self):
        print("Starting")


class Car(Vehicle):
    pass

# Solution: python is case sensitive intead of using uppercasse V in line 27 we use use v so it cause an Name error

class Person:

    def eat(self):
        print("Eating")


class Student(Person):

    def study(self):
        print("Studying")


student = Student()
student.study()

# Solution; we did not add the self word to the study method and Without self, Python cannot correctly bind the instance when calling: