"""Create a simple School Management System.

You must create these classes:

Student
Teacher
Course

Each class must contain:

At least three attributes
At least two methods"""

class Student:

    def study(self):
        print("I want to study math")

    def eat(self):
        print("I want to eat")

student1 = Student()
student1.name = "tola"
student1.id = "123ryeri"
student1.course = "python"



class Teacher:

    def have_class(self):
        print("I have class now")

    def eat(self):
        print("I want to eat")

teacher = Teacher()
teacher.name = "Mr Bolu"
teacher.id = "er455"
teacher.course = "python"
    
class Course:

    def subject(self):
        print('i have class by 9')

    def course_code(self):
        print("python course code is py123")

course1 = Course()
course1.code = "py123"
course1.course_unit = "3 units"
course1.name = "python"