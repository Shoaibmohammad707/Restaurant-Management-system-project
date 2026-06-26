import json

class UpdateOrder:

    def update_order(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)
        except:
            print("No Orders Found")
            return

        if not orders:
            print("No Orders Available")
            return

        order_no = int(input("Enter Order No: ")) - 1

        if order_no < 0 or order_no >= len(orders):
            print("Order Not Found")
            return

        order = orders[order_no]

        print("\nCurrent Order:", order)

        print("\n1. Item  2. Qty  3. Price  4. Size")
        ch = input("Choice: ")

        if ch == "1":
            order["item"] = input("New Item Name: ")

        elif ch == "2":
            order["qty"] = int(input("New Qty: "))
            order["total"] = order["qty"] * order["price"]

        elif ch == "3":
            order["price"] = int(input("New Price: "))
            order["total"] = order["qty"] * order["price"]

        elif ch == "4":
            order["size"] = input("New Size (half/full): ")

        else:
            print("Invalid Choice")
            return

        with open("app/database/orders.json", "w") as file:
            json.dump(orders, file, indent=4)

        print("Order Updated Successfully ")