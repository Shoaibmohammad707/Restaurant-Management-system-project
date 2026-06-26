import json
import uuid
import msvcrt

class Signup:

    def sign_up(self):

        try:
            with open("app/database/userdata.json", "r") as file:
                users = json.load(file)
        except:
            users = []

        user_id = str(uuid.uuid4())[:8]
        print("Generated id:", user_id)

        while True:
            email = input("Enter Email: ")

            if email == "":
                print("Email cannot be empty")
                continue

            if "@" not in email or "." not in email:
                print("Invalid Email Format")
                continue

            break

        while True:

            print("Enter Password: ", end="", flush=True)
            password = ""

            while True:
                ch = msvcrt.getch().decode()

                if ch == "\r":  
                    break

                print("*", end="", flush=True)
                password += ch

            print()

            if len(password) != 6:
                print("Password must be exactly 6 characters")
                continue

            break

        while True:

            print("Confirm Password: ", end="", flush=True)
            confirm_password = ""

            while True:
                ch = msvcrt.getch().decode()

                if ch == "\r":
                    break

                print("*", end="", flush=True)
                confirm_password += ch

            print()

            if password != confirm_password:
                print("Password does not match")
                continue

            break

        while True:
            name = input("Enter Name: ")

            if not name.replace(" ", "").isalpha():
                print("Name should contain only letters")
                continue

            break

        while True:
            address = input("Enter Address: ")

            if address == "":
                print("Address cannot be empty")
                continue

            if address.isdigit():
                print("Invalid Address")
                continue

            break

        while True:
            qualification = input("Enter Qualification: ")

            if qualification == "":
                print("Qualification cannot be empty")
                continue

            break

        users.append({
            "id": user_id,
            "email": email,
            "password": password,
            "name": name,
            "address": address,
            "qualification": qualification,
            "role": "staff"
        })

        with open("app/database/userdata.json", "w") as file:
            json.dump(users, file, indent=4)

        print("Account Created Successfully ")