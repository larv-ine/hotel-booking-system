from hotel import Hotel
from models.room import Room
from models.guest import Guest


def add_room_menu(hotel):
    try:
        number = input("Room number: ").strip()
        if not number:
            print("Room number cannot be empty.")
            return
        room_type = input("Room type (Single/Double/Suite): ").strip()
        price = float(input("Price per night: "))
        if price < 0:
            print("Price cannot be negative.")
            return
        hotel.add_room(Room(number, room_type, price))
        print("Room added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def register_guest_menu(hotel):
    try:
        guest_id = input("Guest ID: ").strip()
        if not guest_id:
            print("Guest ID cannot be empty.")
            return
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        hotel.register_guest(Guest(guest_id, name, phone, email))
        print("Guest registered successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def search_guest_menu(hotel):
    guest_id = input("Enter guest ID to search: ").strip()
    guest = hotel.search_guest(guest_id)
    if guest:
        guest.display_details()
    else:
        print("Guest not found.")


def create_booking_menu(hotel):
    try:
        booking_id = input("Booking ID: ").strip()
        guest_id = input("Guest ID: ").strip()
        room_number = input("Room number: ").strip()
        check_in = input("Check-in date (YYYY-MM-DD): ").strip()
        check_out = input("Check-out date (YYYY-MM-DD): ").strip()
        hotel.create_booking(booking_id, guest_id, room_number, check_in, check_out)
        print("Booking created successfully.")
    except ValueError as e:
        print(f"Booking failed: {e}")


def check_in_menu(hotel):
    booking_id = input("Booking ID to check in: ").strip()
    try:
        hotel.check_in(booking_id)
        print("Guest checked in successfully.")
    except ValueError as e:
        print(f"Check-in failed: {e}")


def check_out_menu(hotel):
    booking_id = input("Booking ID to check out: ").strip()
    try:
        total = hotel.check_out(booking_id)
        print(f"Guest checked out successfully. Total cost: ${total:.2f}")
    except ValueError as e:
        print(f"Check-out failed: {e}")


def main():
    hotel = Hotel()

    menu = """
=================================
   HOTEL CHECK-IN & BOOKING SYSTEM
=================================
1. Add Room
2. Display All Rooms
3. Display Available Rooms
4. Register Guest
5. Search Guest
6. Create Booking
7. Display Bookings
8. Check In
9. Check Out
10. Save & Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_room_menu(hotel)
        elif choice == "2":
            hotel.display_all_rooms()
        elif choice == "3":
            hotel.display_available_rooms()
        elif choice == "4":
            register_guest_menu(hotel)
        elif choice == "5":
            search_guest_menu(hotel)
        elif choice == "6":
            create_booking_menu(hotel)
        elif choice == "7":
            hotel.display_bookings()
        elif choice == "8":
            check_in_menu(hotel)
        elif choice == "9":
            check_out_menu(hotel)
        elif choice == "10":
            hotel.save_all()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()