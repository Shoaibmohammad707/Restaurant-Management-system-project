import json

class ShowAllOrder:

    def show_all_order(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)

        except FileNotFoundError:
            print("No Orders Found")
            return

        if len(orders) == 0:
            print("No Orders Found")
            return

        print("\n" + "=" * 60)
        print(" " * 23 + "ALL ORDERS")
        print("=" * 60)

        for order in orders:

            print("Item  :", order["item"])
            print("Size  :", order["size"])
            print("Qty   :", order["qty"])
            print("Price :", order["price"])
            print("Total :", order["total"])
            print("-" * 60)