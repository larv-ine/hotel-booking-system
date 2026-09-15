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
**Owner:** [Bookings person's name]

| Test ID | Method Being Tested | Scenario Description | Input(s) | Expected Output / Behaviour |
|---|---|---|---|---|
| TC1 | create_booking | Normal valid booking on an available room | room="101" (Available), guest="G1", valid dates | Booking created, room status becomes "Booked" |
| TC2 | create_booking | Attempt to book an already-booked room | room="101" (status="Booked") | Error: room is not available |
| TC3 | create_booking | Attempt to book a room that doesn't exist | room="999" | Error: room not found |
| TC4 | create_booking | Attempt to book with a guest that doesn't exist | guest="G999" | Error: guest not found |
| TC5 | calculate_total_cost | Check-out date before check-in date | check_in="2026-08-25", check_out="2026-08-20" | Error: check-out must be after check-in |


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

## Test Execution Results

| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |
| :--- | :--- | :--- | :--- | :--- |
| **TC1** | Room 101 added successfully | Room 101 added successfully | Pass | Valid room added |
| **TC2** | Error: Room 101 already exists | Error: Room 101 already exists | Pass | Duplicate rejected |
| **TC3** | Error: Price cannot be negative | Error: Price cannot be negative | Pass | Negative input caught |
| **TC4** | Error: Room number cannot be empty | Error: Room number cannot be empty | Pass | Empty string rejected |
| **TC5** | "No available rooms" message shown | "No available rooms" message shown | Pass | Empty state handled |
| **TC6** | Guest G1 registered successfully | Guest G1 registered successfully | Pass | Guest added |
| **TC7** | Error: Guest ID already exists | Error: Guest ID already exists | Pass | Duplicate ID caught |
| **TC8** | Error: Name cannot be empty | Error: Name cannot be empty | Pass | Empty name rejected |
| **TC9** | Error: Invalid phone format | Error: Invalid phone format | Pass | Validation passed |
| **TC10**| Displays all registered guests | Displays all registered guests | Pass | List output verified |
| **TC11**| Booking B1 created for Room 101 | Booking B1 created for Room 101 | Pass | Status changed to Booked |
| **TC12**| Error: Room 101 is already booked | Error: Room 101 is already booked | Pass | Prevents double booking |
| **TC13**| Error: Guest ID G99 does not exist | Error: Guest ID G99 does not exist | Pass | Missing guest caught |
| **TC14**| Guest checked out, Room status: Available | Guest checked out, Room status: Available | Pass | Status reset verified |
| **TC15**| Displays active bookings | Displays active bookings | Pass | Report printed cleanly |
| **TC16**| Data loaded automatically on startup | Data loaded automatically on startup | Pass | File load verified |
| **TC17**| New records saved to disk on exit | New records saved to disk on exit | Pass | Persistence verified |
| **TC18**| Display search result for Room 101 | Display search result for Room 101 | Pass | Search function verified |
| **TC19**| Invalid choice. Please enter a number. | Invalid choice. Please enter a number. | Pass | Exception handling verified |
| **TC20**| Application exits cleanly | Application exits cleanly | Pass | Graceful shutdown |




