# Hotel Room Booking System

A console-based **Hotel Room Booking System** developed in **Python 3**. The program allows users to view available rooms, book a room, generate a bill, and cancel an existing booking. Booking information is stored in a text file so that records can be loaded again when the program starts.

## Project Details

- **Project Title:** Hotel Room Booking System
- **PS No.:** 61
- **Language:** Python 3
- **Concepts Used:** Dictionaries, Lists, Functions, File Handling
- **Interface:** Console-based application

## Room Details

| Room No. | Room Type | Rate per Night |
|---|---|---:|
| 101 | Single Room | ₹2,000 |
| 102 | Double Room | ₹3,500 |
| 201 | Suite Room | ₹6,000 |

**Billing:** GST is calculated at 12% on the room charge.

**Formula:**  
`Room Charge = Rate per Night × Number of Nights`  
`GST = Room Charge × 12%`  
`Total Bill = Room Charge + GST`

## Features

1. **View Available Rooms** – Displays rooms that are not currently booked.
2. **Book a Room** – Takes the guest name, room number, and number of nights, then saves the booking.
3. **Generate Bill** – Calculates the room charge, 12% GST, and final amount.
4. **Cancel Booking** – Cancels an existing booking and makes the room available again.
5. **File Handling** – Saves booking records in `bookings.txt` and loads saved records when the program starts.
6. **Input Validation** – Checks the room number and number of nights and prevents booking an already-booked room.

## Console Menu

```text
===== Hotel Room Booking System =====
1. View available rooms
2. Book a room
3. Generate bill
4. Cancel booking
5. Exit
```

## Test Case Results

The following screenshots show the program's console output for the test scenarios.

### Test Case 1 – Normal Input

- Guest: Amit
- Room: 101
- Nights: 2
- Expected bill: ₹4,000 + ₹480 GST = **₹4,480**

[![Test Case 1 – Normal Input](hotel-room-booking-screenshots/test-case-1-normal-input.jpg)](hotel-room-booking-screenshots/test-case-1-normal-input.jpg)

### Test Case 2 – Boundary / Minimum Input

- Guest: Neha
- Room: 102
- Nights: 1 (minimum)
- Expected bill: ₹3,500 + ₹420 GST = **₹3,920**

[![Test Case 2 – Minimum Input](hotel-room-booking-screenshots/test-case-2-minimum-input.jpg)](hotel-room-booking-screenshots/test-case-2-minimum-input.jpg)

### Test Case 3 – Invalid Input

- Room 101 is already booked by Amit.
- A booking attempt for Room 101 by Neha is rejected.
- Program message: **“Room 101 is already booked. Please choose another room.”**

[![Test Case 3 – Invalid Input](hotel-room-booking-screenshots/test-case-3-invalid-input.jpg)](hotel-room-booking-screenshots/test-case-3-invalid-input.jpg)

### Test Case 4 – Different Valid Scenarios

**View available rooms:** The console displays the available rooms:
- 102 Double – ₹3,500
- 201 Suite – ₹6,000

[![Test Case 4 – View Available Rooms](hotel-room-booking-screenshots/test-case-4-view-available-rooms.jpg)](hotel-room-booking-screenshots/test-case-4-view-available-rooms.jpg)

**Cancel booking:** The booking for Room 101 is cancelled, and the room becomes available again.

[![Test Case 4 – Cancel Booking](hotel-room-booking-screenshots/test-case-4-cancel-booking.jpg)](hotel-room-booking-screenshots/test-case-4-cancel-booking.jpg)

## Project Files

```text
Hotel-Room-Booking-System/
│
├── project-1.py
├── bookings.txt
├── summary.md
└── hotel-room-booking-screenshots/
    ├── project-requirements.jpg
    ├── test-case-1-normal-input.jpg
    ├── test-case-2-minimum-input.jpg
    ├── test-case-3-invalid-input.jpg
    ├── test-case-4-view-available-rooms.jpg
    └── test-case-4-cancel-booking.jpg
```

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code or a terminal.
3. Run:

```bash
python project-1.py
```

4. Follow the menu options shown in the console.

## Assignment Reference

The original problem statement and requirements are included below for reference.

[![Project Requirements](hotel-room-booking-screenshots/project-requirements.jpg)](hotel-room-booking-screenshots/project-requirements.jpg)
