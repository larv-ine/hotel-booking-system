# Test Plan

## Team Members
- [Name 1]
- [Name 2]
- [Name 3]
- [Name 4]

## Selected Project
Project 4 – Hotel Guest Check-In & Room Booking System

---

## Test Cases – Room
**Owner:** SUSAN NJERI MUTHONI

|## Test Cases – Room

**Owner:** SUSAN NJERI MUTHONI

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | `add_room` | Add a room using valid information | room_number="101", room_type="Single", price_per_night=80 | Room 101 is added successfully |
| TC2 | `add_room` | Try to add a room number that already exists | room_number="101" added again | Message shown: "A room with this room number already exists." |
| TC3 | `add_room` | Try to add a room with a negative price | room_number="102", room_type="Double", price_per_night=-50 | Message shown: "Room price cannot be negative." |
| TC4 | `add_room` | Try to add a room with no room number | room_number="", room_type="Single", price_per_night=80 | Message shown: "Room number cannot be empty." |
| TC5 | `display_available_rooms` | No rooms are currently available | all rooms have available=False | Message shown: "No available rooms at the moment." |
*(Rooms owner: add/adjust rows to match the exact validation you implement.)*

---

## Test Cases – Guest
**Owner:** [Guests person's name]

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | register_guest | Normal valid guest is registered | guest_id="G1", name="Alice", phone="0551234567", email="alice@example.com" | Guest registered successfully |
| TC2 | register_guest | Duplicate guest ID rejected | guest_id="G1" registered a second time | Error: guest ID already exists |
| TC3 | register_guest | Empty guest ID rejected | guest_id="" | Error: guest ID cannot be empty |
| TC4 | search_guest | Search for an existing guest | guest_id="G1" | Guest's details displayed |
| TC5 | search_guest | Search for a guest that doesn't exist | guest_id="G999" | "Guest not found." message shown |

*(Guests owner: add/adjust rows to match the exact validation you implement.)*

---

## Test Cases – Booking
**Owner:** [Bookings person's name]

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | create_booking | Normal valid booking on an available room | room="101" (Available), guest="G1", valid dates | Booking created, room status becomes "Booked" |
| TC2 | create_booking | Attempt to book an already-booked room | room="101" (status="Booked") | Error: room is not available |
| TC3 | create_booking | Attempt to book a room that doesn't exist | room="999" | Error: room not found |
| TC4 | create_booking | Attempt to book with a guest that doesn't exist | guest="G999" | Error: guest not found |
| TC5 | calculate_total_cost | Check-out date before check-in date | check_in="2026-08-25", check_out="2026-08-20" | Error: check-out must be after check-in |

*(Bookings owner: add/adjust rows to match the exact validation you implement.)*

---

## Test Cases – Hotel (Check-in / Check-out / File Handling)
**Owner:** [Check-in/out person's name]

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | check_in | Normal check-in on a valid booking | booking_id="B1" (status="Booked") | Booking becomes "Checked-In", room becomes "Occupied" |
| TC2 | check_in | Attempt to check in a booking that's already checked in | booking_id="B1" (status="Checked-In") | Error: guest already checked in |
| TC3 | check_out | Normal check-out on a checked-in booking | booking_id="B1" (status="Checked-In") | Booking becomes "Checked-Out", room becomes "Available", total cost returned |
| TC4 | check_out | Attempt to check out a booking that was never checked in | booking_id="B1" (status="Booked") | Error: guest is not currently checked in |
| TC5 | load_all / save_all | Data persists after restart | add a room, save, close app, reopen app | Previously added room is still present on reload |

*(Check-in/out owner: add/adjust rows to match the exact validation you implement.)*

---

*Note: This Test Plan should be finalized before final testing (Stage 3). Once the application is complete, execute every test case above against the real running app and record the results in `test_results.md`.*
