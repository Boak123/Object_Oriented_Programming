class Temperature:

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        if temperature >= 0:
            self.temperature = temperature
        else:
            print("invalide Input")

    def to_fahrenheit(self):
        F = (self.temperature * 9/5) + 32
        return F

    def display_temperature(self):
        print(self.to_fahrenheit())


temperature1 = Temperature(-2)

print(temperature1.get_temperature())

temperature1.set_temperature(30)

temperature1.display_temperature()
