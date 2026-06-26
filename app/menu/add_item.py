import json

class AddItem:

    def add_item(self):

        try:
            with open("app/database/fooddata.json", "r") as file:
                foods = json.load(file)

        except FileNotFoundError:
            foods = []

        item_name = input("Enter Item Name: ")

        for food in foods:
            if food["item_name"].lower() == item_name.lower():
                print("Item Already Exists")
                return

        half_price = int(input("Enter Half Price: "))
        full_price = int(input("Enter Full Price: "))

        food = {
            "id": len(foods) + 1,
            "item_name": item_name,
            "half_price": half_price,
            "full_price": full_price
        }

        foods.append(food)

        with open("app/database/fooddata.json", "w") as file:
            json.dump(foods, file,indent=4)

        print("Item Added Successfully")