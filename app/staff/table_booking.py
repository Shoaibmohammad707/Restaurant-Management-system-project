import json

class TableBooking:

    def book_table(self):

        name = input("Enter Customer Name: ")
        table_no = input("Enter Table Number: ")
        time = input("Enter Booking Time: ")

        booking = {
            "customer_name": name,
            "table_no": table_no,
            "time": time
        }

        try:
            with open("app/database/table_bookings.json", "r") as file:
                bookings = json.load(file)
        except:
            bookings = []

        bookings.append(booking)

        with open("app/database/table_bookings.json", "w") as file:
            json.dump(bookings, file, indent=4)

        print("Table Booked Successfully ✔")