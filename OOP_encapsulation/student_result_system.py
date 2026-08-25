class Student:

    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    def set_score(self, score):
        self.__score = score
        
        
    def get_score(self):
        return self.__score
    
    def calculate_grade(self):
        if self.__score >= 70:
            return "A"
        elif self.__score >= 60:
            return "B"
        elif self.__score >= 50:
            return "C"
        elif self.__score >= 40:
            return "D"
        elif self.__score >= 0:
            return "F"
        else:
            return "Failed"

    def get_grade(self):
        return self.calculate_grade()
    
    def display_result(self):
        print(f"Name : {self.name}\n"
              f"Student ID : {self.student_id}\n"
              f"Course : {self.course}\n"
              f"Score: {self.__score}\n"
              f"Grade: {self.get_grade()}\n")

student1 = Student("Victor", "ST001", "Python")

student1.set_score(75)

student1.display_result()
    