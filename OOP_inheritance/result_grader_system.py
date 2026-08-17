## University Result System

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, student_id, course, score):
        super().__init__(name)
        self.student_id = student_id
        self.course = course
        self.score = score

    def calculate_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 40:
            return "D"
        return "F"

    def display_result(self):
        print(
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score}\n"
            f"Grade: {self.calculate_grade()}"
        )

    
class Lecturer(Person):
    def __init__(self, name, staff_id, course):
        super().__init__(name)
        self.staff_id = staff_id
        self.course = course

    def grade_student(self, student):
        return student.calculate_grade()


student1 = Student("Victor", "S001", "Math", 85)
student2 = Student("Bolu", "S002", "Physics", 67)
student3 = Student("Tola", "S003", "Biology", 32)

students = [student1, student2, student3]

for student in students:
    student.display_result()
    print("----------")