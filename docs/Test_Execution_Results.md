# Test Execution Results

## 1. Room Management Tests

| Test ID       | Expected Output                         | Actual Output                             | Pass/Fail  | Comments                                          |
| :------------ | :-------------------------------------- | :---------------------------              | :--------  | :----------------------------------               |
| **ROOM-TC01** | Room 101 added successfully             | Room 101 added successfully.              | Pass       | Output matched the expected result.               |
| **ROOM-TC02** | Error message when room number is empty | Room number cannot be empty.              | pass       | Empty room number rejected correctly.             |
| **ROOM-TC03** | Error message when room type is empty   | Invalid input:Room type cannot be empty.  | Pass       | Empty room type rejected correctly.               |
| **ROOM-TC04** | Error: Price cannot be negative         | Price cannot be negative.                 | Pass       | Negative room price rejeced correctly.            |
| **ROOM-TC05** | Room availability changes correctly     | Room 101 became unavailable after booking.| pass       | Room availability changed correctly after booking.|

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

| Test ID        | Expected Output                                  | Actual Output              | Pass/Fail | Comments                   |
| :------------- | :----------------------------------------------- | :------------------------- | :-------- | :------------------------- |
| **HOTEL-TC01** | Room added successfully                          | __________________________ | ______    | __________________________ |
| **HOTEL-TC02** | Duplicate room ID is rejected                    | __________________________ | ______    | __________________________ |
| **HOTEL-TC03** | Guest registered successfully                    | __________________________ | ______    | __________________________ |
| **HOTEL-TC04** | Booking created successfully                     | __________________________ | ______    | __________________________ |
| **HOTEL-TC05** | Already booked/unavailable room cannot be booked | __________________________ | ______    | __________________________ |

## 5. Check-In / Check-Out Tests

| Test ID        | Expected Output                                   | Actual Output              | Pass/Fail | Comments                   |
| :------------- | :------------------------------------------------ | :------------------------- | :-------- | :------------------------- |
| **CHECK-TC01** | Guest successfully checked in                     | __________________________ | ______    | __________________________ |
| **CHECK-TC02** | Error when booking does not exist                 | __________________________ | ______    | __________________________ |
| **CHECK-TC03** | Guest successfully checked out                    | __________________________ | ______    | __________________________ |
| **CHECK-TC04** | Error when booking does not exist during checkout | __________________________ | ______    | __________________________ |
| **CHECK-TC05** | Room becomes available after checkout             | __________________________ | ______    | __________________________ |

## 6. File Handling Tests

| Test ID       | Expected Output                                      | Actual Output              | Pass/Fail | Comments                   |
| :------------ | :--------------------------------------------------- | :------------------------- | :-------- | :------------------------- |
| **FILE-TC01** | Room information is saved to file                    | __________________________ | ______    | __________________________ |
| **FILE-TC02** | Guest information is saved to file                   | __________________________ | ______    | __________________________ |
| **FILE-TC03** | Booking information is saved to file                 | __________________________ | ______    | __________________________ |
| **FILE-TC04** | Information remains after restarting the application | __________________________ | ______    | __________________________ |
| **FILE-TC05** | Updated information is saved correctly               | __________________________ | ______    | __________________________ |

## 7. Exception Handling / Input Validation Tests

| Test ID     | Expected Output                                                   | Actual Output              | Pass/Fail | Comments                   |
| :---------- | :---------------------------------------------------------------- | :------------------------- | :-------- | :------------------------- |
| **EX-TC01** | Error handled when letters are entered where a number is required | __________________________ | ______    | __________________________ |
| **EX-TC02** | Negative room price is rejected                                   | __________________________ | ______    | __________________________ |
| **EX-TC03** | Invalid phone number is rejected                                  | __________________________ | ______    | __________________________ |
| **EX-TC04** | Invalid booking date is rejected                                  | __________________________ | ______    | __________________________ |
| **EX-TC05** | Invalid menu option is handled without crashing                   | __________________________ | ______    | __________________________ |


