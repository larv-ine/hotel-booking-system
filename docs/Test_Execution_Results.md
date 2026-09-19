# Test Execution Results

## 1. Room Management Tests

| Test ID       | Expected Output                         | Actual Output                             | Pass/Fail  | Comments                                          |
| :------------ | :-------------------------------------- | :---------------------------              | :--------  | :----------------------------------               |
| **ROOM-TC01** | Room 101 added successfully             | Room 101 added successfully.              | Pass       | Output matched the expected result.               |
| **ROOM-TC02** | Error message when room number is empty | Room number cannot be empty.              | Pass       | Empty room number rejected correctly.             |
| **ROOM-TC03** | Error message when room type is empty   | Invalid input:Room type cannot be empty.  | Pass       | Empty room type rejected correctly.               |
| **ROOM-TC04** | Error: Price cannot be negative         | Price cannot be negative.                 | Pass       | Negative room price rejeced correctly.            |
| **ROOM-TC05** | Room availability changes correctly     | Room 101 became unavailable after booking.| Pass       | Room availability changed correctly after booking.|

## 2. Guest Management Tests

| Test ID        | Expected Output                | Actual Output              | Pass/Fail | Comments                   |
| :------------- | :----------------------------- | :------------------------- | :-------- | :------------------------- |
| **GUEST-TC01** | Guest registered successfully  | __________________________ | ______    | __________________________ |
| **GUEST-TC02** | Error when guest ID is empty   | __________________________ | ______    | __________________________ |
| **GUEST-TC03** | Error when guest name is empty | __________________________ | ______    | __________________________ |
| **GUEST-TC04** | Error for invalid phone number | __________________________ | ______    | __________________________ |
| **GUEST-TC05** | Error for invalid email        | __________________________ | ______    | __________________________ |

## 3. Booking Tests

| Test ID       | Expected Output                              | Actual Output              | Pass/Fail | Comments                   |
| :------------ | :------------------------------------------- | :------------------------- | :-------- | :------------------------- |
| **BOOK-TC01** | Booking created successfully                 | __________________________ | ______    | __________________________ |
| **BOOK-TC02** | Error for invalid date format                | __________________________ | ______    | __________________________ |
| **BOOK-TC03** | Checkout date cannot be before check-in date | __________________________ | ______    | __________________________ |
| **BOOK-TC04** | Correct number of nights is calculated       | __________________________ | ______    | __________________________ |
| **BOOK-TC05** | Correct total stay cost is calculated        | __________________________ | ______    | __________________________ |

## 4. Hotel Management Tests

| Test ID        | Expected Output                                  | Actual Output                             | Pass/Fail | Comments                   |
| :------------- | :----------------------------------------------- | :-------------------------                | :-------- | :------------------------- |
| **HOTEL-TC01** | Room added successfully                          | Room added successfully.                  | Pass      | Room was added successfully with valid details. |
| **HOTEL-TC02** | Duplicate room ID is rejected                    | Invalid input: Room 201 already exists.   | Pass      | Duplicate room number was rejected correctly. |
| **HOTEL-TC03** | Guest registered successfully                    | Guest registered successfully.            | Pass      | Guest was registered successfully with valid details.|
| **HOTEL-TC04** | Booking created successfully                     | Booking created successfully.             | Pass      | Booking was created successfully for an available room. |
| **HOTEL-TC05** | Already booked/unavailable room cannot be booked | Booking failed: Room 201 is not available.| Pass      | The system correctly prevented an already booked room from being booked again. |

## 5. Check-In / Check-Out Tests

| Test ID        | Expected Output                                   | Actual Output              | Pass/Fail | Comments                   |
| :------------- | :------------------------------------------------ | :------------------------- | :-------- | :------------------------- |
| **CHECK-TC01** | Guest successfully checked in | Guest checked in successfully. | Pass | Correct |
| **CHECK-TC02** | Error when booking does not exist | Check-in failed: Booking B999 not found | Pass | Correct |
| **CHECK-TC03** | Guest successfully checked out | Guest checked out successfully. Total cost: $300.00 | Pass | Correct |
| **CHECK-TC04** | Error when booking does not exist during checkout | Check-out failed: Booking B999 not found | Pass | Correct |
| **CHECK-TC05** | Room becomes available after checkout | Room 202 status shown as Available | Pass | Correct |
## 6. File Handling Tests

| Test ID       | Expected Output                                      | Actual Output              | Pass/Fail | Comments                   |
| :------------ | :--------------------------------------------------- | :------------------------- | :-------- | :------------------------- |
| **FILE-TC01** | Room information is saved to file | Room number: 101,Room type: Single,80.0,True | Fail |
| **FILE-TC02** | Guest information is saved to file | G1,Mercy,124567,mearcy@makau.com | Pass | Correct format, no issues |
| **FILE-TC03** | Booking information is saved to file | B3,G3,203,2026-10-9,2026-10-10,Booked | Pass | Correct format, booking data saved properly |
| **FILE-TC04** | Information remains after restarting the application | Booking B3 shown correctly after restart (Guest G3, Room 203, 2026-10-9 to 2026-10-10, Status: Booked) | Pass | Booking persisted correctly across restart |
|**FILE-TC05** | |Updated information is saved correctly |Updated booking information was saved successfully and the updated details were displayed after restarting the application.|pass|Updated information persisted correctly after saving and restarting.|

## 7. Exception Handling / Input Validation Tests

| Test ID | Expected Output | Actual Output | Pass/Fail | Comments |
| :--- | :--- | :--- | :--- | :--- |

|EX-TC01 | Error handled when letters are entered where a number is required | Invalid input: could not convert string to float: 'aa' | Pass | Invalid non-numeric input was handled without crashing the application. |
| EX-TC02 | Negative room price is rejected | Price cannot be negative. | Pass | Negative room price was rejected correctly by input validation. |
| EX-TC03 | Invalid phone number is rejected | Phone number cannot be negative. | Pass | Invalid phone number was rejected correctly. |
| EX-TC04 | Invalid booking date is rejected | Invalid date format. | Pass | Invalid booking date format was rejected correctly. |
| EX-TC05 | Invalid menu option is handled without crashing | Invalid choice. Please select a valid menu option. | Pass | Invalid menu option was handled without crashing the application. |

