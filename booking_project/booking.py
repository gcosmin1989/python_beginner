class Hotel:
    def __init__(self, name, city, rooms, price):
        self.name = name
        self.city = city
        self.rooms = rooms
        self.price = price
        hotels[self.name] = self

    def __str__(self):
        return f"{self.name} in {self.city}, {self.rooms} rooms at ${self.price} per night"


hotels = {}

def register_hotel():
    name = input('Hotel name: ')
    city = input('City: ')
    rooms = input('Number of rooms: ')
    price = input('Price per night: ')
    Hotel(name, city, rooms, price)
    print(f"Hotel registered: {hotels[name]}")

def booking():
    if hotels:
        print("Booking")
    else:
        print('Sorry, no hotels are available.')
        main()

def main():
    user_choice = input('Would you like to register your Hotel or make a Booking? (Register/Booking)\n').strip().capitalize()

    if user_choice == 'Booking':
        booking()
    elif user_choice == 'Register':
        register_hotel()
    else:
        print('Invalid option. Please choose either "Register" or "Booking".')

if __name__ == "__main__":
        main()
