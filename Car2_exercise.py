#https://pynative.com/python-object-oriented-programming-oop-exercise/
class Vehicle:
    color = 'white'

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self):
        print(f"The seating capacity of the {self.name} is {self.capacity} passengers and the color is {self.color}")

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def seating_capacity(self):
        print(f'The seating capacity of a bus is {self.capacity} passengers')

    def fare(self):
        print(f'Total Bus fare is: {Vehicle.fare(self) * 1.10} ')


class Car(Vehicle):
    pass


schoolBus = Bus('School Volvo', 90, 12, 50)
car1 = Car('BMW', 240, 100, 5)

print(isinstance(schoolBus,Vehicle))
