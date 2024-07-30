class Accommodation:
    def __init__(self, name, city, price):
        self.name = name
        self.city = city
        self.price = price

    def get_info(self):
        return (f'==============================\n'
                f'Registration Successfully for: \n'
                f'Name: {self.name}\n'
                f'City: {self.city}\n'
                f'Price per Night: ${self.price}\n')



