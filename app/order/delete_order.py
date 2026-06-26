import json

class DeleteOrder:

    def delete_order(self):

        with open("app/database/orders.json", "r") as f:
            orders = json.load(f)

        for i, o in enumerate(orders, 1):
            print(i, o["item"], o["qty"])

        n = int(input("Enter Order No: ")) - 1

        orders.pop(n)

        with open("app/database/orders.json", "w") as f:
            json.dump(orders, f, indent=4)

        print("Deleted")