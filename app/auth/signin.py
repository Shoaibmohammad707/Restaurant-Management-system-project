import json
import msvcrt

class Signin:

    def sign_in(self):

        try:
            with open("app/database/userdata.json", "r") as file:
                users = json.load(file)
        except:
            users = []

        while True:

            email = input("Enter Email: ")

            if email == "":
                print("Email cannot be empty")
                continue

            if email == "shoaib123@gmail.com":

                print("Enter Password: ", end="", flush=True)
                password = ""

                while True:
                    ch = msvcrt.getch().decode()

                    if ch == "\r":
                        break

                    print("*", end="", flush=True)
                    password += ch

                print()

                if password == "121121":
                    print("Admin Login Successfully")
                    return "admin"

                print("Wrong Password")
                continue

            email_found = False
            current_user = None

            for user in users:
                if user["email"] == email:
                    current_user = user
                    email_found = True
                    break

            if not email_found:
                print("Email not registered")
                continue

            print("Enter Password: ", end="", flush=True)
            password = ""

            while True:
                ch = msvcrt.getch().decode()

                if ch == "\r":
                    break

                print("*", end="", flush=True)
                password += ch

            print()

            if current_user["password"] != password:
                print("Wrong Password")
                continue

            print("Sign In Successfully")
            print("Welcome", current_user["name"])

            return "staff"