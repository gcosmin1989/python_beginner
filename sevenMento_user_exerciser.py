from datetime import date


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calc_age(self):
        current_year = date.today().year
        year_of_birth = int(self.date_of_birth[-4:])
        return current_year - year_of_birth


pers1 = Person('Cosmin', 'Romania', '31.12.2000')
print('Person:')
print(f'Name: {pers1.name}')
print(f'Country: {pers1.country}')
print(f'Date of birth: {pers1.date_of_birth}')
print(f'Age: {pers1.calc_age()}')
