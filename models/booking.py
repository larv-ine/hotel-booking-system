from datetime import datetime


class Booking:
    """Represents a booking linking a guest to a room for a date range."""

    def __init__(self, booking_id, guest_id, room_number,
                 check_in_date, check_out_date, status="Booked"):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.room_number = room_number
        self.check_in_date = check_in_date    # format: YYYY-MM-DD
        self.check_out_date = check_out_date
        self.status = status  # "Booked", "Checked-In", "Checked-Out"

    def calculate_total_cost(self, price_per_night):
        fmt = "%Y-%m-%d"
        nights = (datetime.strptime(self.check_out_date, fmt) -
                  datetime.strptime(self.check_in_date, fmt)).days
        if nights <= 0:
            raise ValueError("Check-out date must be after check-in date")
        return nights * price_per_night

    def display_details(self):
        print(f"Booking {self.booking_id} | Guest {self.guest_id} | "
              f"Room {self.room_number} | {self.check_in_date} -> "
              f"{self.check_out_date} | Status: {self.status}")

    def to_file_line(self):
        return (f"{self.booking_id},{self.guest_id},{self.room_number},"
                f"{self.check_in_date},{self.check_out_date},{self.status}\n")

    @staticmethod
    def from_file_line(line):
        parts = line.strip().split(",")
        return Booking(*parts)

    def __str__(self):
         return (f"Booking ID: {self.booking_id} | Guest: {self.guest_id} |" \
                f" Room: {self.room_number} |Dates: {self.check_in_date} to "
                f"{self.check_out_date} | Status: {self.status}")