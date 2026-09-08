from models.room import Room
from models.guest import Guest
from models.booking import Booking

ROOMS_FILE = "data/rooms.txt"
GUESTS_FILE = "data/guests.txt"
BOOKINGS_FILE = "data/bookings.txt"


class Hotel:
    """Manages rooms, guests, and bookings for the hotel."""

    def __init__(self):
        self.rooms = []
        self.guests = []
        self.bookings = []
        self.load_all()

    # ---------- ROOMS ----------
    def add_room(self, room):
        if any(r.room_number == room.room_number for r in self.rooms):
            raise ValueError(f"Room {room.room_number} already exists")
        self.rooms.append(room)

    def display_all_rooms(self):
        if not self.rooms:
            print("No rooms found.")
        for r in self.rooms:
            r.display_details()

    def display_available_rooms(self):
        available = [r for r in self.rooms if r.is_available()]
        if not available:
            print("No available rooms.")
        for r in available:
            r.display_details()

    def find_room(self, room_number):
        for r in self.rooms:
            if r.room_number == room_number:
                return r
        return None

    # ---------- GUESTS ----------
    def register_guest(self, guest):
        if any(g.guest_id == guest.guest_id for g in self.guests):
            raise ValueError(f"Guest ID {guest.guest_id} already exists")
        self.guests.append(guest)

    def search_guest(self, guest_id):
        for g in self.guests:
            if g.guest_id == guest_id:
                return g
        return None

    # ---------- BOOKINGS ----------
    def create_booking(self, booking_id, guest_id, room_number, check_in, check_out):
        room = self.find_room(room_number)
        if room is None:
            raise ValueError("Room not found")
        if not room.is_available():
            raise ValueError(f"Room {room_number} is not available")
        if self.search_guest(guest_id) is None:
            raise ValueError("Guest not found")

        booking = Booking(booking_id, guest_id, room_number, check_in, check_out)
        self.bookings.append(booking)
        room.status = "Booked"
        return booking

    def display_bookings(self):
        if not self.bookings:
            print("No bookings found.")
        for b in self.bookings:
            b.display_details()

    def find_booking(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id:
                return b
        return None

    def check_in(self, booking_id):
        booking = self.find_booking(booking_id)
        if booking is None:
            raise ValueError("Booking not found")
        if booking.status == "Checked-In":
            raise ValueError("Guest already checked in")
        if booking.status == "Checked-Out":
            raise ValueError("This booking has already been checked out")

        room = self.find_room(booking.room_number)
        room.status = "Occupied"
        booking.status = "Checked-In"
        return booking

    def check_out(self, booking_id):
        booking = self.find_booking(booking_id)
        if booking is None:
            raise ValueError("Booking not found")
        if booking.status != "Checked-In":
            raise ValueError("Guest is not currently checked in")

        room = self.find_room(booking.room_number)
        total_cost = booking.calculate_total_cost(room.price_per_night)
        room.status = "Available"
        booking.status = "Checked-Out"
        return total_cost

    # ---------- FILE HANDLING ----------
    def save_all(self):
        with open(ROOMS_FILE, "w") as f:
            for r in self.rooms:
                f.write(r.to_file_line())
        with open(GUESTS_FILE, "w") as f:
            for g in self.guests:
                f.write(g.to_file_line())
        with open(BOOKINGS_FILE, "w") as f:
            for b in self.bookings:
                f.write(b.to_file_line())

    def load_all(self):
        try:
            with open(ROOMS_FILE, "r") as f:
                self.rooms = [Room.from_file_line(line) for line in f if line.strip()]
        except FileNotFoundError:
            self.rooms = []

        try:
            with open(GUESTS_FILE, "r") as f:
                self.guests = [Guest.from_file_line(line) for line in f if line.strip()]
        except FileNotFoundError:
            self.guests = []

        try:
            with open(BOOKINGS_FILE, "r") as f:
                self.bookings = [Booking.from_file_line(line) for line in f if line.strip()]
        except FileNotFoundError:
            self.bookings = []