import json
from datetime import datetime

class GenerateBill:

    def cash_payment(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)

        except FileNotFoundError:
            print("No Orders Found")
            return

        if len(orders) == 0:
            print("No Orders Found")
            return

        subtotal = sum(order["total"] for order in orders)
        gst = round(subtotal * 0.05)
        grand_total = subtotal + gst

        date = datetime.now().strftime("%d-%m-%Y")
        time = datetime.now().strftime("%I:%M %p")

        print("\n" + "=" * 70)
        print(" " * 28 + "YOUR BILL")
        print("=" * 70)

        print(f"Date : {date}")
        print(f"Time : {time}")
        print("Payment Method : Cash")

        print("-" * 70)

        print("{:<5} {:<25} {:<10} {:<10} {:<10}".format(
            "ID", "Item Name", "Qty", "Price", "Total"
        ))

        print("-" * 70)

        for i, order in enumerate(orders, start=1):
            print("{:<5} {:<25} {:<10} {:<10} {:<10}".format(
                i,
                order["item"],
                order["qty"],
                order["price"],
                order["total"]
            ))

        print("-" * 70)

        print(f"Subtotal     : ₹{subtotal}")
        print(f"GST (5%)     : ₹{gst}")
        print(f"Grand Total  : ₹{grand_total}")

        print("=" * 70)

    def upi_payment(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)

        except FileNotFoundError:
            print("No Orders Found")
            return

        if len(orders) == 0:
            print("No Orders Found")
            return

        upi_id = input("Enter UPI ID : ")

        subtotal = sum(order["total"] for order in orders)
        gst = round(subtotal * 0.05)
        grand_total = subtotal + gst

        date = datetime.now().strftime("%d-%m-%Y")
        time = datetime.now().strftime("%I:%M %p")

        print("\n" + "=" * 70)
        print(" " * 28 + "YOUR BILL")
        print("=" * 70)

        print(f"Date : {date}")
        print(f"Time : {time}")
        print("Payment Method : UPI")
        print(f"UPI ID : {upi_id}")

        print("-" * 70)

        print("{:<5} {:<25} {:<10} {:<10} {:<10}".format(
            "ID", "Item Name", "Qty", "Price", "Total"
        ))

        print("-" * 70)

        for i, order in enumerate(orders, start=1):
            print("{:<5} {:<25} {:<10} {:<10} {:<10}".format(
                i,
                order["item"],
                order["qty"],
                order["price"],
                order["total"]
            ))

        print("-" * 70)

        print(f"Subtotal     : ₹{subtotal}")
        print(f"GST (5%)     : ₹{gst}")
        print(f"Grand Total  : ₹{grand_total}")

        print("=" * 70)