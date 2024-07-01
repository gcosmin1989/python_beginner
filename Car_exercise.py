class Car:
    #The atributes of the class
    raise_hp = 1.10
    num_of_cars = 0

    def __init__(self, color, model, hp):
        #The atributes of the instance
        self.color = color
        self.model = model
        self.car_status = True
        self.hp = hp
        Car.num_of_cars += 1

    def engine_function(self, status):
        if status == 'OFF' and self.car_status:
            print(f'The car model {self.model} with the color {self.color} has turned {status}')
            self.car_status = False
        elif status == 'OFF' and not self.car_status:
            print(f'The car model {self.model} with the color {self.color} is already turned {status}')
        elif status == 'ON' and not self.car_status:
            print(f'The car model {self.model} with the color {self.color} has turned {status}')
            self.car_status = True
        elif status == 'ON' and self.car_status:
            print(f'The car model {self.model} with the color {self.color} is already turned {status}')

    def check_car(self):
        if self.car_status:
            print('The car is turned on')
        else:
            print('The car is turned off')

    def add_power(self):
        print(f'The horse power of the {self.model} is now {int(self.hp * self.raise_hp)} Horse Power')
        self.hp = self.hp * self.raise_hp

    @classmethod
    def set_hp(cls, amount):
        cls.raise_hp = amount


car1 = Car('red', 'Volvo', 190)
car2 = Car('blue', 'BMW', 200)

print(Car.num_of_cars)
car1.engine_function('OFF')
car1.check_car()
car1.engine_function('OFF')
car1.engine_function('ON')
car1.check_car()
print(car2.hp)
car2.add_power()
Car.set_hp(1.50)
car2.add_power()
car2.add_power()
