class Room:
    """Represents a single hotel room."""

    def __init__(self, room_number, room_type, price_per_night, status="Available"):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.status = status  # "Available", "Booked", "Occupied"

    def is_available(self):
        return self.status == "Available"

    def display_details(self):
        print(f"Room {self.room_number} | {self.room_type} | "
              f"${self.price_per_night}/night | Status: {self.status}")

    def to_file_line(self):
        return f"{self.room_number},{self.room_type},{self.price_per_night},{self.status}\n"

    @staticmethod
    def from_file_line(line):
        room_number, room_type, price, status = line.strip().split(",")
        return Room(room_number, room_type, float(price), status)