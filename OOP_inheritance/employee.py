class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"I am Working with {self.name}")

    def calculate_bonus(self):
        bonus = self.salary * 5 / 100
        return bonus

class Manager(Employee):

    def calculate_bonus(self):
        bonus = self.salary * 15 / 100
        return bonus

class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 10 / 100
        return bonus

employee1 = Employee("Mr Jones", 5000)
manager = Manager("Mr Victor", 4000)
developer1 = Developer("Mr Bolu", 3000)

employees = [employee1, manager, developer1]

for employee in employees:
    employee.work()
    print(employee.calculate_bonus())
    print("----------------")
