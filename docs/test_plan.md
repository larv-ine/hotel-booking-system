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
**Owner:** [Rooms person's name]

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | add_room | Normal valid room is added | room_number="101", type="Single", price=80 | Room added successfully |
| TC2 | add_room | Duplicate room number rejected | room_number="101" added a second time | Error: room already exists |
| TC3 | add_room | Negative price rejected | price=-50 | Error: price cannot be negative |
| TC4 | add_room | Empty room number rejected | room_number="" | Error: room number cannot be empty |
| TC5 | display_available_rooms | No rooms currently available | all existing rooms have status "Booked" or "Occupied" | "No available rooms." message shown |

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

## Test Cases – Hotel (Check-in / Check-out / Booking / File Handling)
**Owner:** [Larvine Mutuku]

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





