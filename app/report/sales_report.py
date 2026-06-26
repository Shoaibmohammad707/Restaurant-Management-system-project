import json

class SalesReport:

    def show_sales_report(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)
        except:
            orders = []

        total_sales = 0

        for order in orders:
            total_sales += order.get("total", 0)

        print("\n===== SALES REPORT =====")
        print("Total Sales:", total_sales)
        print("========================\n")