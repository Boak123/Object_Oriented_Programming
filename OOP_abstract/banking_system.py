from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError

    def get_balance(self):
        return self.__balance

    def _withdraw_amount(self, amount):
        self.__balance -= amount


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount < 0 or self.get_balance() - amount < 10000:
            print("Insufficient balance")
        else:
            self._withdraw_amount(amount)
            print("Successfully withdrawn")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount < 0 or amount > self.get_balance():
            print("Insufficient balance")
        else:
            self._withdraw_amount(amount)
            print("Successfully withdrawn")