class User:

    def __init__(self, username, password):
        self._validate_password(password)
        self.username = username
        self.__password = password

    def change_password(self, old_password, new_password):
        if old_password == self.__password and self._is_valid_password(new_password):
            self.__password = new_password
            return True
        return False

    def check_password(self, password):
        return password == self.__password

    def display_username(self):
        print(f"{self.username}")

    @staticmethod
    def _is_valid_password(password):
        return bool(password) and len(password) >= 8

    @classmethod
    def _validate_password(cls, password):
        if not cls._is_valid_password(password):
            raise ValueError("Password must contain at least 8 characters.")

user = User("Victor", "python123")

print(user.check_password("python123"))       # True

print(user.change_password("python123", "newpassword"))  # True

print(user.check_password("python123"))       # False
print(user.check_password("newpassword"))     # True