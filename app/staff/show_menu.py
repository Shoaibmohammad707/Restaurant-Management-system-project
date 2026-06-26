import json

class ShowMenu:

    def show_menu(self):

        try:
            with open("app/database/fooddata.json", "r") as file:
                foods = json.load(file)

        except FileNotFoundError:
            print("No Data Found")
            return

        if len(foods) == 0:
            print("No Items Available")
            return

        print("=" * 60)
        print(" " * 22 + "VEG FAST FOOD")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[0:16]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))
        print("=" * 60)
        print(" " * 20 + "NON-VEG FAST FOOD")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[16:31]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))

        print("=" * 60)
        print(" " * 21 + "VEG MAIN COURSE")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[31:56]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))

        print("=" * 60)
        print(" " * 20 + "NON VEG MAIN COURSE")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[56:66]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))

        print("=" * 60)
        print(" " * 27 + "ROTI")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[66:76]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))

        print("=" * 60)
        print(" " * 25 + "DESSERTS")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[76:86]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))

        print("=" * 60)
        print(" " * 26 + "DRINKS")
        print("=" * 60)

        print("{:<5} {:<25} {:<15} {:<15}".format(
            "ID", "ITEM NAME", "HALF PRICE", "FULL PRICE"
        ))
        print("-" * 60)

        for food in foods[86:100]:
            print("{:<5} {:<25} {:<15} {:<15}".format(
                food["id"],
                food["item_name"],
                food["half_price"],
                food["full_price"]
            ))

        print("=" * 60)