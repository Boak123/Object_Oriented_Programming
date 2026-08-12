class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):

    def bark(self):
        print("Barking")

dog1 = Dog("jack")
dog1.sleep()
dog1.eat()
dog1.bark()

