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








    
