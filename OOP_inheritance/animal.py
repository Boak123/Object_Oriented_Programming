class Animal:
    def __init__(self, name, makeSound):
        self.name = name
        self.makeSound = makeSound

    def eat(self):
        print("eating")

    def sleep(self):
        print("Sleeping")

    def introduce(self):
        print(f"I am an {self.name}")

class Dog(Animal):

    def introduce(self):
        print(f"I am a {self.name}")

    def make_sound(self):
            print(f"{self.makeSound}")

class Cat(Animal):

    def introduce(self):
        print(f"I am a {self.name}")

    def make_sound(self):
        print(f"{self.makeSound}")

class Bird(Animal):

    def introduce(self):
        print(f"I am a {self.name}")
    def make_sound(self):
        print(f"{self.makeSound}")


dog1 = Dog("jack", "Bark")
cat1 = Cat("jerry", "Meow")
bird1 = Bird("Pigeon", "Chirp")


animal = [dog1, cat1, bird1]

for ani in animal:
    ani.make_sound()