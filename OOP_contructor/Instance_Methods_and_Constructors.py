"""Create a Car class.

Constructor:

brand
color
year

Methods:

start()
stop()
display_information()"""

class Car:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def start(self):
        print(f"{self.brand} is starting.")

    def stop(self):
        print(f"{self.brand} is stopping.")

    def display_information(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Year: {self.year}")

car1 = Car("Toyota", "Blue", 2020)
car1.start()
car1.stop()
car1.display_information()

"""Create a Student class.

Constructor:

name
age
course

Methods:

study()
eat()
display_information()"""

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")

    def eat(self):
        print(f"{self.name} is eating.")

    def display_information(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

student1 = Student("Alice", 20, "Computer Science")
student1.study()
student1.eat()
student1.display_information()