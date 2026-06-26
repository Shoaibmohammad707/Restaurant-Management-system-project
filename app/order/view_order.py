import json

class ViewOrder:

    def view_order(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)
        except:
            print("No Orders Found")
            return

        if not orders:
            print("No Orders Available")
            return

        print("=" * 70)
        print("{:<5} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
            "ID", "ITEM", "SIZE", "QTY", "PRICE", "TOTAL"
        ))
        print("-" * 70)

        for i, order in enumerate(orders, start=1):

            print("{:<5} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
                i,
                order.get("item", "N/A"),
                order.get("size", "N/A"),
                order.get("qty", 0),
                order.get("price", 0),
                order.get("total", 0)
            ))

        print("=" * 70)