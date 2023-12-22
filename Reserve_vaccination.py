def login():
    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        try:
            with open('user_data.txt', 'r') as file:
                users = file.readlines()
                for user in users:
                    user_id, name, user_email, user_password, phone_number, national_id = user.strip().split(", ")
                    if email == user_email and password == user_password:
                        print("Login successful.")
                        print(f"Welcome back, {name}!")
                        return user_id, name, email
                print("Incorrect email or password.")
        except FileNotFoundError:
            print("User data file not found.")
            return None, None, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None, None

def post_login_menu(user_id, name):
    while True:
        print("\nPlease choose one of the following options:")
        print("1. Register vaccination request")
        print("2. Follow up on request")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_vaccination_request(user_id, name)
        elif choice == '2':
            check_appointment(user_id)
        else:
            print("Invalid choice!! Please enter 1 or 2.")

        another_action = input("Would you like to do anything else? (yes/no): ")
        if another_action.lower() in ['no', 'n']:
            print("Done!")
            print(f"Thank you, {name}!")
            return
        elif another_action.lower() not in ['yes', 'y']:
            print("Invalid input!!")

def register_vaccination_request(user_id, name):
    try:
        with open("vaccination_records.txt", "r") as file:
            for line in file:
                values = line.strip().split(", ")
                if user_id in values:
                    print("You have already registered a request.")
                    return

    except FileNotFoundError:
        pass
    try:
        with open("VaccinationCenter.txt", "r") as file:
            centers = file.readlines()
            if not centers:
                print("No vaccination centers available at the moment.")
                return

            print("Available vaccination centers and vaccines:")
            for center in centers:
                center_id, center_name, address, *vaccines = center.strip().split(", ")
                print(f"\nCenter ID: {center_id}")
                print(f"Center Name: {center_name}")
                print(f"Address: {address}")
                print("Available vaccines:")
                for vaccine in vaccines:
                    print(f"-{vaccine}")

        chosen_center = input("\nPlease choose the name of the center: ")
        chosen_vaccine = input("Please choose the vaccine type: ")

        with open("vaccination_records.txt", "a") as file:
            file.write(f"{user_id}, {name}, {chosen_center}, {chosen_vaccine}, Under review\n")

        print("Your request has been registered successfully.")

    except FileNotFoundError:
        print("The VaccinationCenter.txt file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_appointment(user_id):
    appointment_found = False
    try:
        with open("vaccination_records.txt", "r") as file:
            for line in file:
                record_user_id, _, chosen_center, chosen_vaccine, status = line.strip().split(", ")
                if user_id == record_user_id:
                    appointment_details = f"Name center: {chosen_center}, Vaccine: {chosen_vaccine}, Status: {status}"
                    appointment_found = True
                    break

        if appointment_found:
            print("\nHere are the details of your vaccination appointment:")
            print(appointment_details)
        else:
            print("\nNo vaccination appointment found for this User ID.")

    except FileNotFoundError:
        print("\nVaccination records file not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

user_id, name, email = login()
if user_id:
    post_login_menu(user_id, name)
