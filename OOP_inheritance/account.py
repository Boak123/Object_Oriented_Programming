class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        self.balance -= balance

class SavingsAccount(Account):
    def add_interest(self, interest):
        interest = 0
        self.interest += interest

class CurrentAccount(Account):
    def overdraft(self):
        print("over draft")


savingsaccount1 = SavingsAccount(500, 200)
currentaccount1 = CurrentAccount(200, 600)
