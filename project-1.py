# Hotel Room Booking System
# PS No. 61

rooms = {
    101: {"type": "Single", "rate": 2000},
    102: {"type": "Double", "rate": 3500},
    201: {"type": "Suite", "rate": 6000},
}

bookings = []   # har booking ek dictionary hai
FILE_NAME = "bookings.txt"
GST = 12        # percent


def load_bookings():
    """Program start hone par file se bookings padhta hai"""
    try:
        f = open(FILE_NAME, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            booking = {
                "guest": parts[0],
                "room": int(parts[1]),
                "nights": int(parts[2]),
            }
            bookings.append(booking)
        f.close()
    except FileNotFoundError:
        pass    # pehli baar file nahi hogi, koi dikkat nahi


def save_bookings():
    """Har change ke baad bookings file me save karta hai"""
    f = open(FILE_NAME, "w")
    for b in bookings:
        f.write(b["guest"] + "|" + str(b["room"]) + "|" + str(b["nights"]) + "\n")
    f.close()


def is_booked(room_no):
    for b in bookings:
        if b["room"] == room_no:
            return True
    return False


def find_booking(room_no):
    for b in bookings:
        if b["room"] == room_no:
            return b
    return None


def calculate_bill(room_no, nights):
    rate = rooms[room_no]["rate"]
    amount = rate * nights
    gst = amount * GST / 100
    total = amount + gst
    return amount, gst, total


def print_bill(room_no, nights):
    amount, gst, total = calculate_bill(room_no, nights)
    print("Bill: " + str(int(amount)) + " + GST " + str(int(gst)) + " = Rs. " + str(int(total)))


def view_available():
    print("\nAvailable rooms:")
    found = False
    for room_no in rooms:
        if not is_booked(room_no):
            print(room_no, rooms[room_no]["type"], "Rs.", rooms[room_no]["rate"])
            found = True
    if not found:
        print("No rooms available.")


def get_room_number():
    try:
        room_no = int(input("Room: "))
    except ValueError:
        print("Invalid room number.")
        return None
    if room_no not in rooms:
        print("Invalid room number.")
        return None
    return room_no


def book_room():
    name = input("Guest: ").strip()
    if name == "":
        print("Guest name cannot be empty.")
        return

    room_no = get_room_number()
    if room_no is None:
        return

    if is_booked(room_no):
        print("Room " + str(room_no) + " is already booked. Please choose another room.")
        return

    try:
        nights = int(input("Nights: "))
    except ValueError:
        print("Nights must be a number.")
        return
    if nights < 1 or nights > 30:
        print("Nights must be between 1 and 30.")
        return

    bookings.append({"guest": name, "room": room_no, "nights": nights})
    save_bookings()

    night_word = "night" if nights == 1 else "nights"
    print("Room " + str(room_no) + " booked for " + name + " | " + str(nights) + " " + night_word)
    print_bill(room_no, nights)


def cancel_booking():
    room_no = get_room_number()
    if room_no is None:
        return

    booking = find_booking(room_no)
    if booking is None:
        print("Room " + str(room_no) + " has no booking.")
        return

    bookings.remove(booking)
    save_bookings()
    print("Booking for room " + str(room_no) + " cancelled. Room " + str(room_no) + " is now available.")


def generate_bill():
    room_no = get_room_number()
    if room_no is None:
        return

    booking = find_booking(room_no)
    if booking is None:
        print("Room " + str(room_no) + " has no booking.")
        return

    print("Guest:", booking["guest"], "| Room:", room_no, "| Nights:", booking["nights"])
    print_bill(room_no, booking["nights"])


def main():
    load_bookings()
    while True:
        print("\n===== Hotel Room Booking System =====")
        print("1. View available rooms")
        print("2. Book a room")
        print("3. Generate bill")
        print("4. Cancel booking")
        print("5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_available()
        elif choice == "2":
            book_room()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


main()