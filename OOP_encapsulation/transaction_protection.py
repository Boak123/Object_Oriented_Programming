class BankAccount:

    def __init__(self, balance, transaction_count):
        self.__balance = balance
        self.transaction_count = transaction_count

    def deposit(self, amount):
        self.__balance += amount
        self.transaction_count += 1

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transaction_count += 1
            print("Approved")
        else:
            print("Rejected")

    def get_balance(self):
        return self.__balance

    def get_transaction_count(self):
        return self.transaction_count

account1 = BankAccount(10000, 0)
account1.deposit(5000)
account1.get_balance()
account1.withdraw(2000)
account1.get_balance()
account1.withdraw(20000)
account1.get_transaction_count()