import json

class DeleteItem:

    def delete_item(self):

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

                foods.remove(food)
                found = True
                break

        if not found:
            print("Item Not Found")
            return

        with open("app/database/fooddata.json", "w") as file:
            json.dump(foods, file)

        print("Item Deleted Successfully")