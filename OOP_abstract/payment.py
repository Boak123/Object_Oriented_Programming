from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

class BankTransfer(Payment):

    def process_payment(self, amount):
        print(f"Bank transfer: ₦{amount} processed through bank transfer.")

class CardPayment(Payment):

    def process_payment(self, amount):
        print(f"Card payment: ₦{amount} processed through card.")

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Cash payment: ₦{amount} received in cash.")

bank = BankTransfer()
card = CardPayment()
cash = CashPayment()

payments = [bank, card, cash]

for cash in payments:
    cash.process_payment(5000)
