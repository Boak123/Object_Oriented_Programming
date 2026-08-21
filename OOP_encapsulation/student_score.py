class Student:

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("invalid Score")

    def display_result(self):
        print(f"Name: {self.name}\n"
                f"Score: {self.__score}")

student1 = Student("Victor", 85)

print(student1.get_score())

student1.set_score(95)

print(student1.get_score())

student1.set_score(150)

student1.display_result()
