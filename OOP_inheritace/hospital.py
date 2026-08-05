class Person:

    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeping!")

class Doctor(Person):
    pass

class Nurse(Person):
    pass

doctor1 = Doctor()
doctor1.sleep()