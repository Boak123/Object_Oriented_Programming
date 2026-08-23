class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 0 <= salary <= 10000:
            self.__salary = salary
        else:
            print("")

    def increase_salary(self, amount):
        self.__salary += amount

employee = Employee("Victor", 200000)

employee.increase_salary(50000)

print(employee.get_salary())