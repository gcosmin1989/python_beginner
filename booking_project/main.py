from hotel import Hotel
from guesthouse import GuestHouse


def main():
    while True:
        user_choice = input(
            'Would you like to register your Hotel or make a Booking? (Register/Booking/Exit)\n').strip().capitalize()
        if user_choice == 'Booking':
            booking_choice = input('======================================================\n'
                                   'Please choose what accommodation you want:\n'
                                   '\n'
                                   '1 For Hotels\n'
                                   '2 For GuestHouse\n'
                                   '3 Go Back\n'
                                   '======================================================\n')
            if booking_choice == '1':
                Hotel.booking()
            elif booking_choice == '2':
                GuestHouse.booking()
            elif booking_choice == '3':
                main()
        elif user_choice == 'Register':
            accommodation_choice = input('======================================================\n'
                                         'Select the number for your Accommodation Registration: \n'
                                         '  1 For Hotels \n'
                                         '  2 For GuestHouse \n'
                                         '  3 Go Back \n'
                                         '======================================================\n')
            if accommodation_choice == '1':
                hotel_instance = Hotel.register()
                print(hotel_instance.get_info())
            elif accommodation_choice == '2':
                guest_house_instance = GuestHouse.register()
                print(guest_house_instance.get_info())

            elif accommodation_choice == '3':
                main()
        elif user_choice == 'Exit':
            print('Program Closed')
            break
        else:
            print('Invalid option. Please choose either "Register" or "Booking".')


if __name__ == "__main__":
    main()
