import json

class UpdateItem:

    def update_item(self):

        try:
            with open("app/database/fooddata.json", "r") as file:
                foods = json.load(file)

        except FileNotFoundError:
            print("No Data Found")
            return

        item_id = int(input("Enter Item ID: "))

        found = False

        for food in foods:

            if food["id"] == item_id:

                print("\nCurrent Item Details")
                print("Item Name :", food["item_name"])
                print("Half Price:", food["half_price"])
                print("Full Price:", food["full_price"])

                food["half_price"] = int(input("Enter New Half Price: "))
                food["full_price"] = int(input("Enter New Full Price: "))

                found = True
                break

        if not found:
            print("Item Not Found")
            return

        with open("app/database/fooddata.json", "w") as file:
            json.dump(foods, file)

        print("Price Updated Successfully")