from datetime import datetime

#Booking class links a guest to a specific room for a specific date
class Booking:
   DATE_FORMAT="%Y-%m-%d"
   VALID_STATUSES=("Booked", "Checked-In", "Checked-Out")
 
   def __init__(self, booking_id, guest_id, room_number, check_in_date, check_out_date, status="Booked"):

       if not booking_id:
          raise ValueError("Booking ID cannot be empty!")
       if not guest_id:
          raise ValueError("Guest ID cannot be empty")
       if not room_number:
          raise ValueError("Room number cannot be empty")


       try:
          check_in=datetime.strptime(check_in_date, self.DATE_FORMAT)
          check_out=datetime.strptime(check_out_date, self.DATE_FORMAT)
       except ValueError:
          raise ValueError("Invalid date format! Date must be in YYYY-MM-DD") 

       if check_out<=check_in:
          raise ValueError("Check-out Date must be after Check-in date")

       if status not in self.VALID_STATUSES:
          raise ValueError(f"Invalid booking status: {status}")

       self.booking_id = booking_id
       self.guest_id = guest_id
       self.room_number = room_number
       self.check_in_date = check_in_date    # format: YYYY-MM-DD
       self.check_out_date = check_out_date
       self.status = status  # "Booked", "Checked-In", "Checked-Out"
       self._nights = (check_out-check_in).days

   def calculate_total_cost(self, price_per_night): 
      if price_per_night < 0:
           raise ValueError("Price per night cannot be negative")
      return self._nights * price_per_night

   def display_details(self):
        print(self)

   def to_file_line(self):
        return(f"{self.booking_id},"
               f"{self.guest_id},"
               f"{self.room_number},"
               f"{self.check_in_date},"
               f"{self.check_out_date},"
               f"{self.status}\n")

   @staticmethod
   def from_file_line(line):
       parts = line.strip().split(",")
       if len(parts) !=6:
          raise ValueError("Invalid Booking data in file")
       return Booking(*parts)

   def __str__(self):
         return (f"Booking ID: {self.booking_id} | Guest: {self.guest_id} |" \
                 f" Room: {self.room_number} |Dates: {self.check_in_date} to "
                 f"{self.check_out_date} | Status: {self.status}")
       