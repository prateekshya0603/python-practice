class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year =year

    def car_details(self):
        print("Car Detail:", self.model, self.color, self.year)


class SedanCar(Car):
    def __init__(self, roof_top, model, color, year):
        super().__init__(model, color, year)
        self.roof_top = roof_top

    def car_description(self):
        print("Car Detail:", self.roof_top, self.model, self.color, self.year)

    def car_details(self):
        print("I'm in child class")


car1 = Car("Sedan", "red", 1992)
car1.car_details()

SC1 = SedanCar("Yes", "Sedan", "red", 1992)
SC1.car_details()
SC1.car_description()
SC1.car_details()
car1.car_details()

