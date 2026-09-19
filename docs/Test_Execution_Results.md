\# Test Execution Results



\## 1. Room Management Tests



| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |

| :--- | :--- | :--- | :--- | :--- |

| \*\*ROOM-TC01\*\* | Room 101 added successfully | Room 101 added successfully. | Pass | Output matched the expected result. |

| \*\*ROOM-TC02\*\* | Error message when room number is empty | Room number cannot be empty. | Pass | Empty room number was rejected correctly. |

| \*\*ROOM-TC03\*\* | Error message when room type is empty | Invalid input: Room type cannot be empty. | Pass | Empty room type was rejected correctly. |

| \*\*ROOM-TC04\*\* | Error: Price cannot be negative | Price cannot be negative. | Pass | Negative room price was rejected correctly. |

| \*\*ROOM-TC05\*\* | Room availability changes correctly | Room 101 became unavailable after booking. | Pass | Room availability changed correctly after booking. |



\## 2. Hotel Management Tests



| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |

| :--- | :--- | :--- | :--- | :--- |

| \*\*HOTEL-TC01\*\* | Room added successfully | Room added successfully. | Pass | Room was added correctly. |

| \*\*HOTEL-TC02\*\* | Duplicate room is rejected | Invalid input: Room 201 already exists. | Pass | Duplicate room was rejected correctly. |

| \*\*HOTEL-TC03\*\* | Guest registered successfully | Guest registered successfully. | Pass | Guest was registered correctly. |

| \*\*HOTEL-TC04\*\* | Booking created successfully | Booking created successfully. | Pass | Booking was created correctly. |

| \*\*HOTEL-TC05\*\* | Occupied room cannot be booked again | Booking failed: Room 201 is not available. | Pass | System prevented booking of an unavailable room. |



\## 3. Check-In / Check-Out Tests



| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |

| :--- | :--- | :--- | :--- | :--- |

| \*\*CHECK-TC01\*\* | Guest is checked in successfully | Guest checked in successfully. | Pass | Check-in was completed successfully. |

| \*\*CHECK-TC02\*\* | Error when booking does not exist | Check-in failed: Booking B999 not found | Pass | Invalid booking ID was handled correctly. |

| \*\*CHECK-TC03\*\* | Guest is checked out and total cost is calculated | Guest checked out successfully. Total cost: $300.00 | Pass | Check-out and total cost calculation worked correctly. |

| \*\*CHECK-TC04\*\* | Error when booking does not exist | Check-out failed: Booking B999 not found | Pass | Invalid booking ID was handled correctly. |

| \*\*CHECK-TC05\*\* | Room becomes available after check-out | Room 202 status shown as Available | Pass | Room availability was correctly updated after check-out. |



\## 4. File Handling Tests



| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |

| :--- | :--- | :--- | :--- | :--- |

| \*\*FILE-TC01\*\* | Room information is saved to file | Room number: 101, Room type: Single, 80.0, True | Fail | Saved room information did not match the expected file format. |

| \*\*FILE-TC02\*\* | Guest information is saved to file | G1,Mercy,124567,mearcy@makau.com | Pass | Guest information was saved correctly. |

| \*\*FILE-TC03\*\* | Booking information is saved to file | B3,G3,203,2026-10-9,2026-10-10,Booked | Pass | Booking information was saved correctly. |

| \*\*FILE-TC04\*\* | Saved information is loaded after restarting the application | Booking B3, Guest G3, Room 203, dates, Status: Checked-In | Pass | Saved information persisted and was loaded after restarting the application. |

| \*\*FILE-TC05\*\* | Updated information is saved and available after restart | Updated information was displayed after restarting the application. | Pass | Updated information persisted correctly. |



\## 5. Exception Handling / Input Validation Tests



| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |

| :--- | :--- | :--- | :--- | :--- |

| \*\*EX-TC01\*\* | Error handled when letters are entered where a number is required | Invalid input: could not convert string to float: 'aa' | Pass | Invalid non-numeric input was handled without crashing the application. |

| \*\*EX-TC02\*\* | Negative room price is rejected | Price cannot be negative. | Pass | Negative room price was rejected correctly by input validation. |

| \*\*EX-TC03\*\* | Invalid phone number is rejected | Phone number cannot be negative. | Pass | Invalid phone number was rejected correctly. |

| \*\*EX-TC04\*\* | Invalid booking date is rejected | Invalid date format. | Pass | Invalid booking date format was rejected correctly. |

| \*\*EX-TC05\*\* | Invalid menu option is handled without crashing | Invalid choice. Please select a valid menu option. | Pass | Invalid menu option was handled without crashing the application. |



