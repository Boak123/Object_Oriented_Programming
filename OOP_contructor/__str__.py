class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

student1 = Student("Victor", "20")
student2 = Student("Bolu", "21")

print(student1)
print(student2)


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"

book1 = Book("python", "Vickey")
print(book1)


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
            self.balance -= amount

    # def __str__(self):
    #     return f"{self.owner} - {self.balance}"

bankaccount1 = BankAccount("Bolu", 3000)
bankaccount1.deposit(1000)
bankaccount1.withdraw(500)

class Inventory:

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def update_stock(self):
        print("Stock updated")

    def __str__(self):
        return f"{self.product_name}, {self.price}, {self.quantity}"

stock1 = Inventory("Perfume", "100", "50")
print(stock1)