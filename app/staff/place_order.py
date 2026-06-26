import json
from datetime import datetime

class PlaceOrder:

    def __init__(self):
        self.orders = []
        self.total = 0

    def place_order(self):

        with open("app/database/fooddata.json", "r") as file:
            foods = json.load(file)

        name = input("Enter Item Name: ").strip().lower()

        found = False

        for food in foods:

            if food["item_name"].strip().lower() == name:

                print("\nEnter Size (half/full):")
                size = input("Type half or full: ").strip().lower()

                if size == "half":
                    price = food["half_price"]

                elif size == "full":
                    price = food["full_price"]

                else:
                    print("Invalid Size (only half/full allowed)")
                    return

                qty = input("Enter Quantity: ").strip()

                if not qty.isdigit():
                    print("Invalid Quantity")
                    return

                qty = int(qty)

                order = {
                    "item": food["item_name"],
                    "size": size,
                    "qty": qty,
                    "price": price,
                    "total": price * qty,
                    "date": datetime.now().strftime("%Y-%m-%d")
                }

                self.orders.append(order)

                self.total += price * qty

                try:
                    with open("app/database/orders.json", "r") as file:
                        data = json.load(file)

                except:
                    data = []

                data.append(order)

                with open("app/database/orders.json", "w") as file:
                    json.dump(data, file, indent=4)

                print("\nOrder Added Successfully")

                found = True
                break

        if not found:
            print("\nItem Not Found")