"""
Create a Car class with a constructor.

It should accept:

brand
color
year

Then create two objects.

Do not worry about methods yet.

I'll review your solution afterward. 🚀"""

class Car():

    def __init__(self, brand, color, year):
        self.brand = brand
        self.c0lor = color
        self.year = year

car1 = Car("toyota", "blue", "2020")
car2 = Car("Honda", "black", "2019")

"""Create a Book class.

The constructor should receive:

title
author
pages

Create two books and print all their attributes.

Take your time and write the code yourself. 🚀"""

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("python", "bolu", 300)
book2 = Book("C++", "john doe", 456)
