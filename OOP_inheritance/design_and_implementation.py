"""You're designing the system yourself.

Scenario

A university wants a simple Payment System.

There are three types of people who can receive payments:

Person
├── Student
├── Lecturer
└── Administrator

Every person has:

name
account_number

Every class must have:

receive_payment()

But the behavior must be different:

Student

Receives payment and prints:

Victor received ₦50000 as student allowance.
Lecturer

Receives payment and prints:

Bolu received ₦300000 as lecturer salary.
Administrator

Receives payment and prints:

Tola received ₦200000 as administrator salary."""

class Person:
    def __init__(self, name, account_number, amount):
        self.name = name
        self.account_number = account_number
        self.amount = amount

    def receive_payment(self, amount):
        self.amount = amount
        print(f"{self.name} received ₦{self.amount} as student allowance.")
   
class Student(Person):
    def receive_payment(self):
        print(f"{self.name} received ₦{self.amount} as student allowance.")
   
class Lecturer(Person):
    def receive_payment(self):
        print(f"{self.name} received ₦{self.amount} as Lecturer salary")

class Administrator(Person):
    def receive_payment(self):
        print(f"{self.name} received ₦{self.amount} as administrator salary")

student1 = Student("Victor", 23456789, 10000)
lecturer1 = Lecturer("Mr Jones", 678903566, 20000)
administrator1 = Administrator("Mr Jack", 567891234, 25000)

people = [student1, lecturer1, administrator1]

for person in people:
    person.receive_payment()


