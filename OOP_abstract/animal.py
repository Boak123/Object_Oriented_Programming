from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Dog says Bark")

class Cat(Animal):

    def make_sound(self):
        print("Cat says Meow")
    
dog = Dog()
cat = Cat()

sound = [dog, cat]
for animal in sound:
    animal.make_sound()
