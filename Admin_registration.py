def login():
    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        try:
            with open('admin_data.txt', 'r') as file:
                users = file.readlines()
                user_data = None

                for user in users:
                    user_id, name, user_email, user_password, phone_number, national_id = map(str.strip,
                                                                                              user.split(","))
                    if email == user_email and password == user_password:
                        print("Login successful.")
                        user_data = {
                            "user_id": user_id,
                            "name": name,
                            "email": user_email,
                            "phone_number": phone_number,
                            "user_password": user_password
                        }
                        break

                if user_data is None:
                    print("Incorrect email or password. Please try again.")
                else:
                    return user_data

        except FileNotFoundError:
            print("User data file not found.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def display_user_profile(user_data):
    print("\nUser Profile:")
    print(f"ID: {user_data['user_id']}")
    print(f"Name: {user_data['name']}")
    print(f"Email: {user_data['email']}")
    print(f"Password: {user_data['user_password']}")

def display_vaccine_administration():
    import Vaccine_Administration

user_data = login()
if user_data:
    print(f"\nWelcome, {user_data['name']}!")
    while True:
        choice = input("\nChoose an option:\n1. View Profile\n2. Vaccine Administration\nEnter your choice: ")
        if choice == '1':
            display_user_profile(user_data)
        elif choice == '2':
            import Vaccine_Administration
        else:
            print("Invalid choice!! Please enter 1 or 2.")

        continue_service = input("Do you require any other service? (yes/no): ").lower()
        while continue_service not in ['yes', 'y', 'no', 'n']:
            continue_service = input("Invalid input!! Please enter yes or no: ").lower()

        if continue_service in ['no', 'n']:
            print(f"Goodbye, {user_data['name']}.")
            break