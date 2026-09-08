class Guest:
    """Represents a hotel guest."""

    def __init__(self, guest_id, name, phone, email):
        self.guest_id = guest_id
        self.name = name
        self.phone = phone
        self.email = email

    def display_details(self):
        print(f"Guest {self.guest_id} | {self.name} | {self.phone} | {self.email}")

    def to_file_line(self):
        return f"{self.guest_id},{self.name},{self.phone},{self.email}\n"

    @staticmethod
    def from_file_line(line):
        guest_id, name, phone, email = line.strip().split(",")
        return Guest(guest_id, name, phone, email)