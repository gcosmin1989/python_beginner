class Vehicle():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print('The engine has started')

    def stop_engine(self):
        print('The engine has stopped')


class Car(Vehicle):
    def __init__(self, brand, model, year, num_of_doors):
        super().__init__(brand, model, year)
        self.num_of_doors = num_of_doors

    def lock_doors(self):
        print('The doors are locked')

    def unlock_doors(self):
        print('The doors are unlocked')


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type_bike):
        super().__init__(brand, model, year)
        self.type_bike = type_bike

    def ring_bell(self):
        print('Ring Ring!')


car1 = Car('Ford', 'Focus', 2016, 5)
car1.lock_doors()
car1.unlock_doors()

bike1 = Bicycle('Cube', '3', 2022, 'MountainBike')
bike1.ring_bell()
