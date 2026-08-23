class Student:

    def __init__(self, name, attendance):
        self.name = name
        self.__attendance = attendance

    def attend_class(self):
        self.__attendance += 1

    def get_attendance(self):
        return self.__attendance

    def set_attendance(self, attendance):
        if 0 <= attendance <= 100:
            self.__attendance = attendance
        else:
            print("")

    def display_attendance(self):
        print(self.get_attendance())

student1 = Student("Victor", 5)
student1.get_attendance()
student1.set_attendance(5)
student1.display_attendance()