from app.auth.signup import Signup
from app.auth.signin import Signin
from app.menu.add_item import AddItem
from app.menu.show_item import ShowItem
from app.menu.update_item import UpdateItem
from app.menu.delete_item import DeleteItem
from app.order.view_order import ViewOrder
from app.order.update_order import UpdateOrder
from app.order.delete_order import DeleteOrder

signup_obj = Signup()
signin_obj = Signin()
add_item_obj = AddItem()
show_item_obj = ShowItem()
update_item_obj = UpdateItem()
delete_item_obj = DeleteItem()

view_order_obj = ViewOrder()
update_order_obj = UpdateOrder()
delete_order_obj = DeleteOrder()

from app.report.daily_report import DailyReport
from app.report.sales_report import SalesReport

daily_obj = DailyReport()
sales_obj = SalesReport()

from app.staff.show_menu import ShowMenu
from app.staff.place_order import PlaceOrder
from app.staff.generate_bill import GenerateBill
from app.staff.show_all_order import ShowAllOrder
from app.staff.table_booking import TableBooking

table_obj = TableBooking()
show_all_order_obj = ShowAllOrder()
menu_obj = ShowMenu()
order_obj = PlaceOrder()
bill_obj = GenerateBill()

def generate_bill_menu():

    while True:

        print("\n====================")
        print("   GENERATE BILL")
        print("====================")

        print("1. Cash Payment")
        print("2. UPI Payment")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            bill_obj.cash_payment()

        elif choice == "2":
            bill_obj.upi_payment()

        elif choice == "3":
            break

        else:
            print("Invalid Choice")
            
def take_order():

    while True:

        print("\n====================")
        print("     TAKE ORDER")
        print("====================")

        print("1. Show Menu")
        print("2. Place Order")
        print("3. Show All Orders")
        print("4. Generate Bill")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            menu_obj.show_menu()

        elif choice == "2":
            order_obj.place_order()

        elif choice == "3":
            show_all_order_obj.show_all_order() 

        elif choice == "4":
            generate_bill_menu()
       
        elif choice == "5":
            break

        else:
            print("Invalid Choice")

def report_menu():

    while True:

        print("\n" + "=" * 52)
        print("\t\tREPORT SYSTEM")
        print("=" * 52)

        print("\n\t1. Daily Report")
        print("\t2. Sales Report")
        print("\t3. Back")

        print("\n" + "=" * 52)

        choice = input("Enter your choice: ")

        if choice == "1":
            daily_obj.show_daily_report()

        elif choice == "2":
            sales_obj.show_sales_report()

        elif choice == "3":
            break

        else:
            print("Invalid Choice")

def order_management():

    while True:

        print("=" * 52)
        print("\t\tORDER MANAGEMENT")
        print("=" * 52)

        print("\n\t1. View All Orders")
        print("\t2. Update Order")
        print("\t3. Delete Order")
        print("\t4. Back")

        print("\n" + "=" * 52)

        choice = input("Enter your choice: ")

        if choice == "1":
            view_order_obj.view_order()

        elif choice == "2":
            update_order_obj.update_order()

        elif choice == "3":
            delete_order_obj.delete_order()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

def menu_management():

    while True:

        print("=" * 52)
        print("\t\tMENU MANAGEMENT")
        print("=" * 52)

        print("\n\t1. Show Item")
        print("\t2. Add Item")
        print("\t3. Update Item")
        print("\t4. Delete Item")
        print("\t5. Back")

        print("\n" + "=" * 52)

        choice = input("Enter your choice: ")

        if choice == "1":
            show_item_obj.show_item()

        elif choice == "2":
            add_item_obj.add_item()

        elif choice == "3":
            update_item_obj.update_item()

        elif choice == "4":
            delete_item_obj.delete_item()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")

def admin_dashboard():

    while True:

        print("=" * 52)
        print("\t\tADMIN DASHBOARD")
        print("=" * 52)

        print("\n\t1. MENU MANAGEMENT")
        print("\t2. ORDER MANAGEMENT")
        print("\t3. REPORT SYSTEM")
        print("\t5. EXIT")

        print("\n" + "=" * 52)

        choice = input("Enter your choice: ")

        if choice == "1":
            menu_management()

        elif choice == "2":
            order_management()

        elif choice == "3":
            report_menu()

        elif choice == "5":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

def staff_dashboard():

    while True:

        print("=" * 52)
        print("\t\tSTAFF DASHBOARD")
        print("=" * 52)

        print("\n\t1. TAKE ORDER")
        print("\t2. TABLE BOOKING")
        print("\t3. EXIT")

        print("\n" + "=" * 52)

        choice = input("Enter your choice: ")

        if choice == "1":
            take_order()

        elif choice == "2":
            table_obj.book_table()


        elif choice == "3":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

while True:

    print("=" * 52)
    print("\t\tREGISTRATION MENU")
    print("=" * 52)

    print("\n\t1. SIGNUP")
    print("\t2. SIGNIN")
    print("\t3. EXIT")

    print("\n" + "=" * 52)

    choice = input("Enter your choice: ")

    if choice == "1":
        signup_obj.sign_up()

    elif choice == "2":
        role = signin_obj.sign_in()

        if role == "admin":
            admin_dashboard()

        elif role == "staff":
            staff_dashboard()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")