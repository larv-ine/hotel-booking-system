class Room:
    def __init__(self, room_number, room_type, price):
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

room1 = Room("101", "Single", 50)
room1.display_room()


room1 = Room("101", "Single", 50)

print(room1.room_number)
print(room1.room_type)
print(room1.price)
print(room1.available)
room1.display_room()

    
