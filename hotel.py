from models.room import Room
from models.guest import Guest
from models.booking import Booking

ROOMS_FILE = "data/rooms.txt"
GUESTS_FILE = "data/guests.txt"
BOOKINGS_FILE = "data/bookings.txt"


class Hotel:
    """Manages all rooms, guests, and bookings for the hotel."""

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
            return
        for r in self.rooms:
            r.display_details()

    def display_available_rooms(self):
        available = [r for r in self.rooms if r.is_available()]
        if not available:
            print("No available rooms.")
            return
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
        # Prevent two bookings from using the same booking ID
        if any(b.booking_id == booking_id for b in self.bookings):
            raise ValueError(f"Booking ID {booking_id} already exists")

        room = self.find_room(room_number)
        if room is None:
            raise ValueError(f"Room {room_number} not found")
        if not room.is_available():
            raise ValueError(f"Room {room_number} is not available")
        if self.search_guest(guest_id) is None:
            raise ValueError(f"Guest {guest_id} not found")

        booking = Booking(booking_id, guest_id, room_number, check_in, check_out)
        self.bookings.append(booking)
        room.status = "Booked"
        return booking

    def display_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return
        for b in self.bookings:
            b.display_details()

    def find_booking(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id:
                return b
        return None

    # ---------- CHECK-IN / CHECK-OUT ----------
    def check_in(self, booking_id):
        booking = self.find_booking(booking_id)
        if booking is None:
            raise ValueError(f"Booking {booking_id} not found")
        if booking.status == "Checked-In":
            raise ValueError("Guest already checked in")
        if booking.status == "Checked-Out":
            raise ValueError("This booking has already been checked out")

        room = self.find_room(booking.room_number)
        if room is None:
            raise ValueError("The room for this booking no longer exists")

        room.status = "Occupied"
        booking.status = "Checked-In"
        return booking

    def check_out(self, booking_id):
        booking = self.find_booking(booking_id)
        if booking is None:
            raise ValueError(f"Booking {booking_id} not found")
        if booking.status != "Checked-In":
            raise ValueError("Guest is not currently checked in")

        room = self.find_room(booking.room_number)
        if room is None:
            raise ValueError("The room for this booking no longer exists")

        total_cost = booking.calculate_total_cost(room.price_per_night)
        room.status = "Available"
        booking.status = "Checked-Out"
        return total_cost

    # ---------- FILE HANDLING ----------
    def save_all(self):
        try:
            with open(ROOMS_FILE, "w") as f:
                for r in self.rooms:
                    f.write(r.to_file_line())
            with open(GUESTS_FILE, "w") as f:
                for g in self.guests:
                    f.write(g.to_file_line())
            with open(BOOKINGS_FILE, "w") as f:
                for b in self.bookings:
                    f.write(b.to_file_line())
        except OSError as e:
            print(f"Warning: could not save data. {e}")

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