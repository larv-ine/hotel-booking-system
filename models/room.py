class Room:
    def __init__(self, room_number, room_type, price_per_night):
        if not room_number:
            raise ValueError("Room number cannot be empty.")

        if not room_type:
            raise ValueError("Room type cannot be empty.")

        if price_per_night < 0:
            raise ValueError("Room price cannot be negative.")

        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.available = True

    def display_room(self):
        status = "Available" if self.available else "Occupied"

        print(f"Room Number: {self.room_number}")
        print(f"Room Type: {self.room_type}")
        print(f"Price per Night: ${self.price_per_night:.2f}")
        print(f"Status: {status}")

 # Allows Hotel class to use display_details()
    def display_details(self):
        self.display_room()

    def make_unavailable(self):
        self.available = False

    def make_available(self):
        self.available = True


# Add a new room
def add_room(rooms, room_number, room_type, price_per_night):
    if room_number in rooms:
        print("A room with this room number already exists.")
        return

    try:
        new_room = Room(room_number, room_type, price_per_night)
        rooms[room_number] = new_room
        print(f"Room {room_number} added successfully.")

    except ValueError as error:
        print(error)


# Display all rooms
def display_all_rooms(rooms):
    if not rooms:
        print("No rooms available.")
        return

    for room in rooms.values():
        room.display_room()


# Display available rooms
def display_available_rooms(rooms):
    found_available_room = False

    for room in rooms.values():
        if room.available:
            room.display_room()
            found_available_room = True

    if not found_available_room:
        print("No available rooms at the moment.")


# Save rooms to a file
def save_rooms(rooms):
    try:
        with open("Data/rooms.txt", "w") as file:
            for room in rooms.values():
                file.write(
                    f"{room.room_number},{room.room_type},"
                    f"{room.price_per_night},{room.available}\n"
                )

        print("Rooms saved successfully.")

    except OSError as error:
        print(f"Error saving rooms: {error}")


# Load rooms from a file
def load_rooms():
    rooms = {}

    try:
        with open("Data/rooms.txt", "r") as file:
            for line in file:
                room_number, room_type, price_per_night, available = line.strip().split(",")

                room = Room(
                    room_number,
                    room_type,
                    float(price_per_night)
                )

                room.available = available == "True"

                rooms[room_number] = room

    except FileNotFoundError:
        print("No room file found. Starting with no rooms.")

    return rooms