from accomodation import Accommodation


class GuestHouse(Accommodation):
    guest_houses = {}

    def __init__(self, name, city, price, beds, owner_name):
        super().__init__(name, city, price)
        self.beds = beds
        self.owner_name = owner_name
        GuestHouse.guest_houses[self.name] = self

    def get_info(self):
        accommodation_info = super().get_info()
        return f'{accommodation_info}Number of beds: {self.beds}\nOwner: {self.owner_name}'

    @staticmethod
    def register():
        name = input('Guest House name: ')
        city = input('City: ')
        price = int(input('Price per night: '))
        beds = int(input('Number of beds: '))
        owner_name = input('GuestHouse owner name: ')

        return GuestHouse(name, city, price, beds, owner_name)

    @staticmethod
    def booking():
        if not GuestHouse.guest_houses:
            print("No GuestHouses available for booking")
            return
        print("List of GuestHouses:")
        for i, (guest_house_name, guest_house) in enumerate(GuestHouse.guest_houses.items(), 1):
            print(
                f"{i}. GuestHouse: {guest_house_name}, City: {guest_house.city}, Price: ${guest_house.price}, Owner: {guest_house.owner_name}")

        chosen_guest_house_name = input("Choose the GuestHouse you want to stay in (enter the GuestHouse name): ")
        if chosen_guest_house_name in GuestHouse.guest_houses:
            chosen_guest_house = GuestHouse.guest_houses[chosen_guest_house_name]
            print(
                f"Available Beds for {chosen_guest_house.name} in {chosen_guest_house.city} is {chosen_guest_house.beds} beds at ${chosen_guest_house.price} per night.")
            number_of_beds = int(input('How many beds do you want? '))

            if number_of_beds > chosen_guest_house.beds:
                print("Not enough beds available.")
                return
            chosen_guest_house.beds -= number_of_beds
            number_of_days = int(input('How many days do you want to stay?'))
            print(f"You booked {number_of_beds} beds for {number_of_days} days, the total cost is ${number_of_beds * chosen_guest_house.price * number_of_days}")
        else:
            print("Guest house not found.")
