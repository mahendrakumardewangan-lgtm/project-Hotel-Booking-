# Hotel Room Booking System

A console-based hotel room booking application written in **Python 3**. The user can view available rooms, book a room for a number of nights, cancel a booking and generate the bill. All booking details are saved in a file, so they are not lost when the program is closed.

**Name:** Mahendra Kumar  
**ERP No.:** RU-26-00150  
**PS No.:** 61  
**University:** Rungta International Skills University, B.Tech Computer Science and Engineering

---

## What the Project Does

- Shows the list of rooms that are currently available.
- Books a room for a guest for 1 to 30 nights.
- Cancels an existing booking, which makes the room available again.
- Generates the bill for a booked room.
- Saves every booking to `bookings.txt` after each change and loads the saved bookings when the program starts.
- Validates the input and does not allow a room to be booked twice.

## Rooms and Billing

| Room No. | Type | Rate per night |
|----------|--------|----------------|
| 101 | Single | Rs. 2000 |
| 102 | Double | Rs. 3500 |
| 201 | Suite | Rs. 6000 |

**Bill = (rate x nights) + 12% GST**

Example: Room 101 for 2 nights = 4000 + GST 480 = **Rs. 4480**

## Python Concepts Used

- **Dictionaries:** room details are stored in the `rooms` dictionary.
- **Lists:** current bookings are stored in the `bookings` list (each booking is a dictionary).
- **Functions:** viewing, booking, cancelling and billing are done through separate functions.
- **File Handling:** bookings are written to and read from `bookings.txt`.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python hotel_booking.py
```

## Menu

```
===== Hotel Room Booking System =====
1. View available rooms
2. Book a room
3. Generate bill
4. Cancel booking
5. Exit
```

## Sample Run

```
Enter choice: 2
Guest: Amit
Room: 101
Nights: 2
Room 101 booked for Amit | 2 nights
Bill: 4000 + GST 480 = Rs. 4480
```

## Validation

- Room number must be 101, 102 or 201.
- Nights must be a number between 1 and 30.
- Guest name cannot be empty.
- A room that is already booked cannot be booked again.
- Cancelling or billing a room that has no booking shows a message.

## Functions

| Function | Purpose |
|----------|---------|
| `load_bookings()` | Reads bookings.txt at program start |
| `save_bookings()` | Writes all bookings to bookings.txt |
| `is_booked(room_no)` | Checks whether a room is already booked |
| `find_booking(room_no)` | Returns the booking of a room |
| `calculate_bill(room_no, nights)` | Calculates amount, GST and total |
| `print_bill(room_no, nights)` | Prints the bill |
| `view_available()` | Shows the rooms that are not booked |
| `get_room_number()` | Takes the room number and validates it |
| `book_room()` | Books a room after validation |
| `cancel_booking()` | Cancels the booking of a room |
| `generate_bill()` | Generates the bill for a booked room |
| `main()` | Shows the menu and calls the functions |

## Test Cases

| # | Scenario | Result |
|---|----------|--------|
| 1 | Normal input: Amit, room 101, 2 nights | Room 101 booked for Amit \| 2 nights. Bill: 4000 + GST 480 = Rs. 4480 |
| 2 | Minimum input: Neha, room 102, 1 night | Room 102 booked for Neha \| 1 night. Bill: 3500 + GST 420 = Rs. 3920 |
| 3 | Invalid input: room 101 already booked | Room 101 is already booked. Please choose another room. |
| 4 | Different valid scenario: view rooms, then cancel room 101 | Rooms 102 and 201 shown. Booking for room 101 cancelled. Room 101 is now available. |

All 4 test cases passed.

## Project Files

```
hotel_booking.py     # main program
bookings.txt         # saved bookings (created automatically)
README.md            # this file
```

## Future Improvements

- Date-wise booking
- Customer login
- Graphical user interface (GUI)
