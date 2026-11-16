
# Hotel Room Booking System - Project Summary

| | |
|---|---|
| **Name** | Mahendra Kumar |
| **ERP No.** | RU-26-00150 |
| **PS No.** | 61 |
| **University** | Rungta International Skills University (B.Tech CSE) |
| **Language** | Python 3 |

---

## 1. Overview

A console application for a hotel. The user can:

- View the available rooms
- Book a room for a number of nights
- Cancel a booking
- Generate the bill

All bookings are saved in `bookings.txt`, so the data is not lost when the program closes.

## 2. Objective

To build a simple and working Hotel Room Booking System using the Python concepts of **Dictionaries, Lists, Functions and File Handling**.

## 3. Room Details and Billing Rules

| Room No. | Type | Rate per night |
|----------|--------|----------------|
| 101 | Single | Rs. 2000 |
| 102 | Double | Rs. 3500 |
| 201 | Suite | Rs. 6000 |

- **Bill = (rate x nights) + 12% GST**
- Nights must be between **1 and 30**
- A room can have only one booking at a time

## 4. Approach and Logic

- Room details are stored in a **dictionary** called `rooms` (room number is the key).
- Current bookings are stored in a **list of dictionaries** called `bookings` (guest, room, nights).
- The menu runs inside a `while` loop until the user chooses Exit.
- After every booking or cancellation, the list is written to `bookings.txt`.
- When the program starts, the bookings are loaded back from the file.
- File line format: `guest|room|nights`

## 5. Functions

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

## 6. Validation

- Room number must be a number and one of 101, 102 or 201.
- Nights must be a number between 1 and 30.
- Guest name cannot be empty.
- An already booked room cannot be booked again.
- Cancelling or asking for a bill of a room with no booking shows a message.

## 7. Menu and How to Run

```
1. View available rooms
2. Book a room
3. Generate bill
4. Cancel booking
5. Exit
```

Run the program with: `python hotel_booking.py`

## 8. Test Cases (4 out of 4 passed)

### Test Case 1: Normal Input

| Input | Expected Output |
|-------|-----------------|
| Menu option 2 (Book), Guest: Amit, Room: 101, Nights: 2 | Room 101 booked for Amit \| 2 nights<br>Bill: 4000 + GST 480 = Rs. 4480 |

**Actual Output:**
![Uploading WhatsApp Image 2026-11-16 at 4.59.46 PM.jpeg…]()

```
Room 101 booked for Amit | 2 nights
Bill: 4000 + GST 480 = Rs. 4480
```

**Screenshot:**

<!-- Add Tes<img width="1366" height="768" alt="WhatsApp Image 2026-11-16 at 4 59 46 PM" src="https://github.com/user-attachments/assets/ced7dc18-f084-4428-8743-01a4cf5a1b6e" />
t Case 1 screenshot here, for example: ![Test Case 1](screenshots/image.jpg) -->





### Test Case 2: Boundary / Minimum Input

| Input | Expected Output |
|-------|-----------------|
| Menu option 2 (Book), Guest: Neha, Room: 102, Nights: 1 (minimum) | Room 102 booked for Neha \| 1 night<br>Bill: 3500 + GST 420 = Rs. 3920 |

**Actual Output:**

```
Room 102 booked for Neha | 1 night
Bill: 3500 + GST 420 = Rs. 3920
```

**Screenshot:**
<img width="1366" height="768" alt="WhatsApp Image 2026-11-16 at 4 59 49 PM" src="https://github.com/user-attachments/assets/1d3f46c7-a596-468e-8a8f-d530cb189478" />

<!-- Add Test Case 2 screenshot here, for example: ![Test Case 2](screenshots/image.jpg) -->





### Test Case 3: Invalid Input

| Input | Expected Output |
|-------|-----------------|
| Room 101 is already booked by Amit. Menu option 2 (Book), Guest: Neha, Room: 101, Nights: 3 | Room 101 is already booked. Please choose another room. |

**Actual Output:**

```
Room 101 is already booked. Please choose another room.
```

**Screenshot:**

<!-- Add Test Case 3 screenshot here, for example: ![Test Case 3](screenshots/image.jpg) --><img width="1366" height="768" alt="WhatsApp Image 2026-11-16 at 4 59 49 PM (1)" src="https://github.com/user-attachments/assets/f32ff454-d29a-4831-af1c-a498d139ce62" />






### Test Case 4: Different Valid Scenario

| Input | Expected Output |
|-------|-----------------|
| bookings.txt has: Room 101 - Amit - 2 nights<br>(a) Menu option 1 (Available rooms)<br>(b) Menu option 4 (Cancel): Room 101 | (a) 102 Double Rs. 3500, 201 Suite Rs. 6000<br>(b) Booking for room 101 cancelled. Room 101 is now available. |

**Actual Output (a): Available rooms**

```
Available rooms:
102 Double Rs. 3500
201 Suite Rs. 6000
```

**Screenshot:**
<img width="1366" height="768" alt="WhatsApp Image 2026-11-16 at 4 59 49 PM (2)" src="https://github.com/user-attachments/assets/603911bb-df91-42e7-8fc3-8912bd6fd1f3" />

<!-- Add Test Case 4 (a) screenshot here, for example: ![Test Case 4 (a)](screenshots/image.jpg) -->





**Actual Output (b): Cancel room 101**

```
Booking for room 101 cancelled. Room 101 is now available.
```

**Screenshot:**

<!-- Add Test Case 4 (b) screenshot here, for example: ![Test Case 4 (b)](screenshots/image.jpg) -->

<img width="1366" height="768" alt="WhatsApp Image 2026-11-16 at 4 59 49 PM (3)" src="https://github.com/user-attachments/assets/27e19975-667a-488f-a00c-fd36b059a60d" />




**Result:** All 4 actual outputs match the expected outputs.

## 9. Conclusion

The project works as required. It supports viewing rooms, booking, cancellation and bill generation, and it stores the data safely in a file. It helped in learning how to use dictionaries, lists, functions and file handling together in Python.

**Future improvements:** date-wise booking, customer login and a GUI.
