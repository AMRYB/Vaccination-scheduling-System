def prompt_yes_no(question):
    response = input(question).lower()
    while response not in ['yes', 'no']:
        response = input("Please enter yes or no: ").lower()
    return response == 'yes'

def prompt_for_center_data():
    center_id = input("Enter the center ID: ")
    name = input("Enter the center name: ")
    address = input("Enter the center address: ")
    vaccines = input("Enter the list of vaccines (separated by commas): ").split(',')
    return center_id, name, address, vaccines

def add_center_to_file(center_data):
    with open('VaccinationCenter.txt', 'a') as file:
        file.write(f"{center_data[0]}, {center_data[1]}, {center_data[2]}, {', '.join(center_data[3])}\n")
    print("Center added successfully.")

def remove_center_from_file(center_id):
    with open('VaccinationCenter.txt', 'r') as file:
        centers = file.readlines()
    with open('VaccinationCenter.txt', 'w') as file:
        centers_removed = 0
        for center in centers:
            if not center.startswith(center_id):
                file.write(center)
            else:
                centers_removed += 1
        if centers_removed == 0:
            print("No center found with the given ID.")
        else:
            print("Center removed successfully.")

def search_center_by_name(name):
    with open('VaccinationCenter.txt', 'r') as file:
        centers = file.readlines()
        found = False
        for center in centers:
            if name.lower() in center.lower():
                print(f"Found center: {center}")
                found = True
        if not found:
            print("No center found with the given name.")

def list_registered_users():
    try:
        with open('vaccination_records.txt', 'r') as file:
            users = file.readlines()
            if users:
                print("Registered Users:")
                for user in users:
                    user_info = user.strip().split(',')
                    print(f"User ID:{user_info[0]}, Name:{user_info[1]}, Vaccine place:{user_info[2]}")
            else:
                print("No registered users found.")
    except FileNotFoundError:
        print("No reservations recorded!!")

def manage_reservations():
    try:
        with open('vaccination_records.txt', 'r') as file:
            reservations = file.readlines()
        if not reservations:
            print("No reservation requests found.")
            return

        for i, reservation in enumerate(reservations):
            user_info = reservation.strip().split(',')
            if user_info[-1].strip() == "Under review":
                print(f"Request {i + 1}: ID:{user_info[0]}, Name:{user_info[1]}, Center:{user_info[2]}, Vaccine:{user_info[3]}")
                approval = prompt_yes_no("Do you approve this reservation? (yes/no): ")
                if approval:
                    appointment_date = input("Enter the appointment date (YYYY-MM-DD): ")
                    user_info[-1] = appointment_date
                else:
                    user_info[-1] = "Rejected"
                reservations[i] = ', '.join(user_info) + '\n'

        with open('vaccination_records.txt', 'w') as file:
            file.writelines(reservations)
        print("Reservations have been updated.")
    except FileNotFoundError:
        print("No reservations recorded!!")


def main_menu():
    while True:
        print("1: Manage vaccination centers (Add/Remove)")
        print("2: Search for a vaccination center by name")
        print("3: List registered users")
        print("4: Accept reservation and schedule vaccination date")
        print("5: Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_choice = input("Do you want to add (A) or remove (R) a vaccination center? (A/R): ").upper()
            if manage_choice == 'A':
                center_data = prompt_for_center_data()
                add_center_to_file(center_data)
            elif manage_choice == 'R':
                center_id = input("Enter the center ID to remove: ")
                remove_center_from_file(center_id)
            else:
                print("Invalid selection, please choose A to add or R to remove.")
        elif choice == '2':
            name = input("Enter the name of the vaccination center to search for: ")
            search_center_by_name(name)
        elif choice == '3':
            list_registered_users()
        elif choice == '4':
            manage_reservations()
        elif choice == '5':
            break
        else:
            print("Invalid choice!! please enter a number between 1 and 5.")


main_menu()

