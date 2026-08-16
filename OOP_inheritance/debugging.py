# challeng 8 

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        print(f"I am {self.name}, studying {self.course}")


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"I am {self.name}, I teach {self.subject}")


class Administrator(Person):

    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def introduce(self):
        print(f"I am {self.name}, I work in {self.department}")


student = Student("Victor", 20, "Python")
teacher = Teacher("Bolu", 35, "Computer Science")
administrator = Administrator("Tola", 40, "Administration")

people = [student, teacher, administrator]

for person in people:
    person.introduce()

# we did not put self in line 20 and 40 instead of self.course or self.department we only put course and department
# And in line 16 we supposed to put 3 positional 