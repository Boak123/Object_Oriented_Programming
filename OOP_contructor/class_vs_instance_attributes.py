"""Create a Car class.

Class attribute:

manufacturer = "Toyota"

Instance attributes:

brand
color
year

Create two objects and print all the values."""

class Car:

    manufacturer = "Toyota" #class attribute

    def __init__(self, brand, color, year):
        self.brand = brand #instance attribute
        self.color = color #instance attribute
        self.year = year #instance attribute

car1 = Car("Toyota", "Blue", 2020)
car2 = Car("Honda", "Red", 2021)

print(car1.brand, car1.color, car1.year, car1.manufacturer)
print(car2.brand, car2.color, car2.year, car2.manufacturer)


"""Create an Employee class.

Class attribute:

company = "OpenAI"

Instance attributes:

name
department
salary

Methods:

work()
display_information()"""

class Employee:

    company = "OpenAI"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def work(self):
        print("I went to work")

    def display_information(self):
        print(f"Name: {self.name}"
        "Nepartment: {self.department}"
        "Salary: {self.salary}")

employee1 = Employee("Boluwatife Vctor", "Programmer", 100000)
employee1.work()
employee1.display_information()
