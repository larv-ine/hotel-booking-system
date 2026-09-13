class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True

room1 = Room("101", "Single", 50)

print(room1.room_number)
print(room1.room_type)
print(room1.price)
print(room1.available)

    
   