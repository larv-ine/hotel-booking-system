# Test Plan

## Team Members
 - Larvine Mutuku
-  Susan Muthoni
- Hazel Awino
- Yusra Haruna 

**Date:** September 2026


## Selected Project

Project 4 – Hotel Guest Check-In & Room Booking System

---

## Test Cases – Room
**Owner:** Susan Njeri Muthoni

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | `add_room` | Add a room using valid information | room_number="101", room_type="Single", price_per_night=80 | Room 101 is added successfully |
| TC2 | `add_room` | Try to add a room number that already exists | room_number="101" added again | Message shown: "A room with this room number already exists." |
| TC3 | `add_room` | Try to add a room with a negative price | room_number="102", room_type="Double", price_per_night=-50 | Message shown: "Room price cannot be negative." |
| TC4 | `add_room` | Try to add a room with no room number | room_number="", room_type="Single", price_per_night=80 | Message shown: "Room number cannot be empty." |
| TC5 | `display_available_rooms` | No rooms are currently available | all rooms have available=False | Message shown: "No available rooms at the moment." |


---

## Test Cases – Guest
**Owner:** Yusra Haruna

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | register_guest | Normal valid guest is registered | guest_id="G1", name="Alice", phone="0551234567", email="alice@example.com" | Guest registered successfully |
| TC2 | register_guest | Duplicate guest ID rejected | guest_id="G1" registered a second time | Error: guest ID already exists |
| TC3 | register_guest | Empty guest ID rejected | guest_id="" | Error: guest ID cannot be empty |
| TC4 | search_guest | Search for an existing guest | guest_id="G1" | Guest's details displayed |
| TC5 | search_guest | Search for a guest that doesn't exist | guest_id="G999" | "Guest not found." message shown |



---

## Test Cases – Booking
**Owner:** Hazel Awino

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | `__init__` | Normal valid booking creation | booking_id="B1", guest_id="G1", room_number="101", check_in="2026-09-20", check_out="2026-09-25", status="Booked" | Booking object created successfully with all attributes set correctly |
| TC2 | `__init__` | Invalid case: empty booking_id | booking_id="" | Error: "Booking ID cannot be empty!" |
| TC3 | `__init__` | Invalid case: badly formatted date | check_in="20-09-2026" | Error: "Invalid date format! Date must be in YYYY-MM-DD" |
| TC4 | `__init__` | Edge case: check-out date equal to check-in date | check_in="2026-09-20", check_out="2026-09-20" | Error: "Check-out Date must be after Check-in date" |
| TC5 | `__init__` | Invalid case: invalid status value | status="Boked" | Error: "Invalid booking status: Boked" |
| TC6 | `calculate_total_cost` | Normal valid cost calculation | check_in="2026-09-20", check_out="2026-09-25", price_per_night=100 | Returns 500 (5 nights × 100) |
| TC7 | `calculate_total_cost` | Invalid case: negative price per night | price_per_night=-50 | Error: "Price per night cannot be negative" |
| TC8 | `from_file_line` | Invalid case: malformed file line (wrong number of fields) | line="B1,G1,101\n" | Error: "Invalid Booking data in file" |


---

## Test Cases – Hotel (Check-in / Check-out / Booking / File Handling)
**Owner:** Larvine Mutuku

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | check_in | Normal check-in on a valid booking | booking_id="B1" (status="Booked") | Booking becomes "Checked-In", room becomes "Occupied" |
| TC2 | check_in | Attempt to check in a booking that's already checked in | booking_id="B1" (status="Checked-In") | Error: "Guest is already checked in for this booking" |
| TC3 | check_in | Attempt to check in with a booking ID that doesn't exist | booking_id="B999" | Error: "Booking B999 not found" |
| TC4 | check_out | Normal check-out on a checked-in booking | booking_id="B1" (status="Checked-In") | Booking becomes "Checked-Out", room becomes "Available", correct total cost returned |
| TC5 | check_out | Attempt to check out a booking that was never checked in | booking_id="B1" (status="Booked") | Error: "Guest is not currently checked in for this booking" |
| TC6 | create_booking | Attempt to create a booking with a duplicate booking ID | booking_id="B1" used a second time | Error: "Booking ID B1 already exists" |
| TC7 | save_all / load_all | Data persists after restart | Add a room, save, close app, reopen app | Previously added room is still present on reload |
| TC8 | load_all | App starts for the first time with no data files present | No rooms.txt/guests.txt/bookings.txt exist yet | App starts normally with empty lists, no crash | 


---

