# Class Design Document

## Team Members
- Larvine Mutuku
-  Susan Muthoni
- Hazel Awino
- Yusra Haruna 


**Date:** September 2026

## Selected Project
Project 4 – Hotel Guest Check-In & Room Booking System

---

## Class 1: Room
**Owner:** SUSAN NJERI MUTHONI

**Purpose:** Represents a hotel room and stores its room number, room type, price per night, and current availability. The class also allows the room to be marked as available or unavailable.

### Attributes
| Attribute | Data Type | Description |
|---|---|---|
| room_number | str | Unique number used to identify the hotel room |
| room_type | str | Category of the room, such as Single, Double, or Suite |
| price_per_night | float | Cost of staying in the room for one night |
| available | bool | Indicates the availability of the room. True means the room is available, while False means it is unavailable or occupied |

### Methods
| Method | Parameters | Purpose |
|---|---|---|
| `__init__` | room_number, room_type, price_per_night | Creates a new Room object. It validates that the room number and room type are not empty and that the price per night is not negative. New rooms are available by default. |
| `display_room` | none | Displays the room number, room type, price per night, and current availability status |
| `make_unavailable` | none | Changes the room's availability to False when the room becomes unavailable or occupied |
| `make_available` | none | Changes the room's availability to True when the room becomes available again |

### Room Management Functions

| Function | Parameters | Purpose |
|---|---|---|
| `add_room` | rooms, room_number, room_type, price_per_night | Creates a new Room object and adds it to the rooms dictionary. It also prevents duplicate room numbers. |
| `display_all_rooms` | rooms | Displays all rooms stored in the system |
| `display_available_rooms` | rooms | Displays only rooms whose `available` value is True |
| `save_rooms` | rooms | Saves the room number, room type, price per night, and availability of each room to `Data/rooms.txt` |
| `load_rooms` | none | Reads room information from `Data/rooms.txt`, recreates the Room objects, restores their availability status, and returns the rooms dictionary |

---

## Class 2: Guest
**Owner:** Yusra Haruna

**Purpose:** Represents a hotel guest and their contact details.

### Attributes
| Attribute | Data Type | Description |
|---|---|---|
| guest_id | str | Unique identifier for the guest |
| name | str | Guest's full name |
| phone | str | Guest's contact phone number |
| email | str | Guest's contact email address |

### Methods
| Method | Parameters | Purpose |
|---|---|---|
| `__init__` | guest_id, name, phone, email | Creates a new Guest object and validates the input |
| `display_details` | none | Prints the guest's information to the screen |
| `to_file_line` | none | Converts the guest's data into a line of text for saving to a file |
| `from_file_line` | line (str) | Rebuilds a Guest object from a saved line of text |

---


## Class 3: Booking
**Owner:** [Bookings person's name]

**Purpose:** Links a Guest to a Room for a given date range and tracks the booking's status.

### Attributes
| Attribute | Data Type | Description |
|---|---|---|
| booking_id | str | Unique identifier for the booking |
| guest_id | str | ID of the guest who made the booking |
| room_number | str | Number of the room being booked |
| check_in_date | str | Planned/actual check-in date (YYYY-MM-DD) |
| check_out_date | str | Planned/actual check-out date (YYYY-MM-DD) |
| status | str | Current state: "Booked", "Checked-In", or "Checked-Out" |

### Methods
| Method | Parameters | Purpose |
|---|---|---|
| `__init__` | booking_id, guest_id, room_number, check_in_date, check_out_date, status | Creates a new Booking object; validates that IDs are non-empty, dates are in the correct format, check-out is after check-in, and status is one of the allowed values |
| `calculate_total_cost` | price_per_night | Returns the total stay cost (nights ├ù price); raises an error if price_per_night is negative |
| `display_details` | none | Prints the booking's information to the screen |
| `to_file_line` | none | Converts the booking's data into a line of text for saving to a file |
| `from_file_line` | line (str) | Rebuilds a Booking object from a saved line of text |



---
## Class 4: Hotel
**Owner:** [Larvine Mutuku]

**Purpose:** The central manager class. Holds all rooms, guests, and bookings, applies business rules (e.g. preventing double-booking and duplicate IDs), coordinates check-in/check-out, and handles saving/loading all data to and from files.

### Attributes
| Attribute | Data Type | Description |
|---|---|---|
| rooms | list of Room | All rooms currently in the hotel |
| guests | list of Guest | All registered guests |
| bookings | list of Booking | All bookings made |

### Methods
| Method | Parameters | Purpose |
|---|---|---|
| `__init__` | none | Initialises empty lists and loads any previously saved data from file |
| `add_room` | room | Adds a new room, prevents duplicate room numbers |
| `display_all_rooms` | none | Prints every room |
| `display_available_rooms` | none | Prints only rooms with status "Available" |
| `find_room` | room_number | Returns the Room object matching the given number, or None |
| `register_guest` | guest | Adds a new guest, prevents duplicate guest IDs |
| `search_guest` | guest_id | Returns the Guest object matching the given ID, or None |
| `create_booking` | booking_id, guest_id, room_number, check_in, check_out | Validates the booking ID is unique, the room exists and is available, and the guest exists. Creates a Booking and marks the room "Booked" |
| `display_bookings` | none | Prints every booking |
| `find_booking` | booking_id | Returns the Booking object matching the given ID, or None |
| `check_in` | booking_id | Validates the booking exists, hasn't already been checked in/out, and its room still exists. Marks booking "Checked-In" and room "Occupied" |
| `check_out` | booking_id | Validates the booking exists, guest is currently checked in, and the room still exists. Calculates total cost, marks booking "Checked-Out", frees the room |
| `save_all` | none | Writes all rooms, guests, and bookings to their data files; catches file-write errors |
| `load_all` | none | Reads all rooms, guests, and bookings from their data files on startup; handles missing files gracefully |


---

## Class Diagram
![Class Diagram](class_diagram.png)
- Hotel → manages → Room
- Hotel → manages → Guest
- Hotel → manages → Booking
- Booking → references → Room
- Booking → references → Guest
