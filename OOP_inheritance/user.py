class User:

    def create_account(self):
        print("Account Created")

    def sign_in(self):
        print("Signed In")

    def sign_out(self):
        print("Signed Out")

class Admin(User):
    pass

class Customer(User):
    pass

