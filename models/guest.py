class Guest:
    """Represents a hotel guest and their contact details."""

    def __init__(self, guest_id, name, phone, email):
        if not guest_id or not guest_id.strip():
            raise ValueError("Guest ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Guest name cannot be empty.")
        if not phone or not phone.strip():
            raise ValueError("Phone number cannot be empty.")
        if not phone.strip().isdigit():
            raise ValueError("Phone number must contain digits only.")
        if not email or "@" not in email:
            raise ValueError("Email must be a valid address (must contain '@').")

        self.guest_id = guest_id.strip()
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()

    def display_details(self):
        """Prints a formatted summary of the guest."""
        print(f"Guest {self.guest_id} | {self.name} | {self.phone} | {self.email}")

    def to_file_line(self):
        """Returns a comma-separated line for saving to a file."""
        return f"{self.guest_id},{self.name},{self.phone},{self.email}\n"

    @staticmethod
    def from_file_line(line):
        """
        Builds a Guest object from a saved comma-separated line.
        Raises ValueError if the line is malformed or missing fields.
        """
        try:
            guest_id, name, phone, email = line.strip().split(",")
        except ValueError:
            raise ValueError(f"Malformed guest record, skipping: {line.strip()}")

        return Guest(guest_id, name, phone, email)