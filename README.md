# Hotel Guest Check-In & Room Booking System

## Project Description

The **Hotel Guest Check-In & Room Booking System** is a Python-based application developed to help a small hotel manage rooms, guests, bookings, check-ins, and check-outs.

The system allows hotel staff to manage hotel information through a menu-based interface while storing important information in files so that data can be loaded again when the application is restarted.

## Team Members

* **Larvine Mutuku**
* **[Susan Muthoni ]**
* **[Yusra Haruna]**
* **[ Hazel Awino]**

## Main Features

The application provides the following features:

* Add hotel rooms
* Display all rooms
* Display available rooms
* Register guests
* Search for guests
* Create room bookings
* Display bookings
* Check guests into rooms
* Check guests out
* Prevent occupied or unavailable rooms from being booked
* Calculate the total cost of a stay
* Save room, guest, and booking information to files
* Load saved information when the application starts
* Validate user input and handle errors

## Classes Used

### Room

Represents a hotel room and stores information such as the room number, room type, price, and availability.

### Guest

Represents a hotel guest and stores the guest's relevant registration information.

### Booking

Represents a room booking and manages information such as the guest, room, dates, number of nights, and total stay cost.

### Hotel

Manages the overall hotel system, including rooms, guests, bookings, check-ins, check-outs, and related operations.

## Files Used

The project contains Python source files for the application and data files for persistent storage.

* `main.py` — Runs the main menu and application.
* `hotel.py` — Contains the main hotel management functionality.
* `models/` — Contains the classes used by the application.
* `Data/` — Stores room, guest, and booking information.
* `docs/` — Contains project documentation such as the class design, class diagram, test plan, and test execution results.

## How to Run the Application

### Requirements

* Python 3.x
* A Python-compatible IDE such as VS Code

### Steps

1. Clone or download the GitHub repository.
2. Open the project folder in VS Code or another Python IDE.
3. Open the terminal in the project directory.
4. Run the application using:

```bash
python main.py
```

5. Follow the menu options displayed by the application.

## Documentation

The `docs` folder contains the supporting project documentation:

* Class Design Document
* Class Diagram
* Test Plan
* Test Execution Results

## Team Contributions

### Larvine Mutuku

-Check-in/check-out functionality
-File handling
-Testing and documentation
###  Susan Muthoni

-Room management functionality
-Room class
-Testing
### Yusra Haruna


-Guest management functionality
-Guest class
-Input validation
### Hazel Awino

-Booking functionality
-Booking class
-Booking testing
## Academic Integrity

This project represents the team's own understanding and effort. Course materials, official Python documentation, and other learning resources were used to support learning and development.


