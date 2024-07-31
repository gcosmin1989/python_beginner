from accomodation import Accommodation


class Hotel(Accommodation):
    hotels = {}

    def __init__(self, name, city, rooms, price):
        super().__init__(name, city, price)
        self.rooms = rooms
        Hotel.hotels[self.name] = self

    def get_info(self):
        accommodation_info = super().get_info()
        return f'{accommodation_info}Number of rooms:{self.rooms}\n'

    @staticmethod
    def register():
        name = input('Hotel name: ')
        city = input('City: ')
        rooms = int(input('Number of rooms: '))
        price = int(input('Price per night: '))
        return Hotel(name, city, rooms, price)

    @staticmethod
    def booking():
        if not Hotel.hotels:
            print("No hotels available for booking")
            return
        print("List of hotels:")
        for i, (hotel_name, hotel) in enumerate(Hotel.hotels.items(), 1):
            print(f"{i}. Hotel: {hotel_name}, City: {hotel.city}, Price: ${hotel.price}")

        chosen_hotel_name = input("Choose the hotel you want to stay in (enter the hotel name): ")

        if chosen_hotel_name in Hotel.hotels:
            chosen_hotel = Hotel.hotels[chosen_hotel_name]
            print(
                f"Available Rooms for {chosen_hotel.name} in {chosen_hotel.city} is {chosen_hotel.rooms} rooms at ${chosen_hotel.price} per night.")
            number_of_rooms = int(input('How many rooms do you want? \n'))
            if number_of_rooms > chosen_hotel.rooms:
                print("Not enough rooms available.")
                return
            chosen_hotel.rooms -= number_of_rooms
            number_of_days = int(input('How many days do you want to stay?: \n'))
            print(f"You booked {number_of_rooms} rooms for {number_of_days} days, the total cost is ${number_of_rooms * chosen_hotel.price * number_of_days}")
        else:
            print("Hotel not found.")
