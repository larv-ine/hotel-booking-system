class Room:
    def __init__(self, room_number, room_type, price):
        if not room_number:
            raise ValueError("Room number cannot be empty.")

        if not room_type:
            raise ValueError("Room type cannot be empty.")

        if price < 0:
            raise ValueError("Room price cannot be negative.")

        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True

    def display_room(self):
        status = "Available" if self.available else "Occupied"

        print(f"Room Number: {self.room_number}")
        print(f"Room Type: {self.room_type}")
        print(f"Price per Night: ${self.price:.2f}")
        print(f"Status: {status}")

    def make_unavailable(self):
        self.available = False

    def make_available(self):
        self.available = True

#Add a new room
def add_room(rooms, room_number, room_type, price):
    if room_number in rooms:
        print("A room with this room number already exists.")
        return

    try:
        new_room = Room(room_number, room_type, price)
        rooms[room_number] = new_room
        print(f"Room {room_number} added successfully.")

    except ValueError as error:
        print(error)

# Display all rooms.
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










    
