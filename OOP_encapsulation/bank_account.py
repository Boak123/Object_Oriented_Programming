class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print(f"Balance: {self.__balance}")

account = BankAccount("Victor", 50000)

account.deposit(20000)
account.withdraw(15000)
account.withdraw(100000)

account.display_account()