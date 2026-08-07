class Account:

    def deposit(self):
        print("Deposited")
    def withdraw(self):
        print("Withdrawed")

class SavingsAccount(Account):

    def save_money(self):
        print("Saved")

account1 = SavingsAccount()
account1.save_money()
account1.withdraw()