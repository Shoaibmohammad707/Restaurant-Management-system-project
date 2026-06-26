import json
from datetime import datetime

class DailyReport:

    def show_daily_report(self):

        try:
            with open("app/database/orders.json", "r") as file:
                orders = json.load(file)
        except:
            orders = []

        today = datetime.now().strftime("%Y-%m-%d")

        today_orders = [
            order for order in orders
            if order.get("date") == today
        ]

        print("\n===== DAILY REPORT =====")
        print("Date:", today)
        print("Total Orders:", len(today_orders))
        print("========================")