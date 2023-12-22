def check_user():
    response = input("Have you used the application before? (y/n): ")

    if response.lower() == 'y':
        import Reserve_vaccination
    elif response.lower() == 'n':
        user_id = input("Enter your ID: ")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Create a password: ")
        phone_number = input("Enter your phone number: ")
        national_id = input("Enter your national ID: ")

        confirm = input("Are you sure you want to register with this information? (y/n): ")

        if confirm.lower() == 'y':
            user_data = f"{user_id}, {name}, {email}, {password}, {phone_number}, {national_id}\n"

            with open('user_data.txt', 'a') as file:
                file.write(user_data)
            print("User registered successfully.")
            import Reserve_vaccination
        else:
            print("Registration canceled!!")
    else:
        print("Invalid input!!")
        check_user()

check_user()
