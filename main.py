while True:
    choice = input("Choose (a) for Admin or (u) for User: ")

    if choice == 'a':
        import Admin_registration
        break
    elif choice == 'u':
        import User_registration
        break
    else:
        print("Invalid choice!!")
