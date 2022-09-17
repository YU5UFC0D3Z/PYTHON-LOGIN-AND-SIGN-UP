user_db = {
    "Easypy3":["Easypy3", "easypy3@chasefx.co.uk"]
    }
    
option = input("""
Menue:
1. Register
2. Login

Select menue option: """)

while option == "1":
    print("\nRegister -")

    while True:
        reg_user = input("\nEnter username: ")
        reg_user = reg_user.capitalize()

        if reg_user in user_db:
            print("Username already exists!")
        elif len(reg_user) < 4 or len(reg_user) > 20:
            print("Username must be between 4 - 20 characters!")
        elif reg_user[0].isalpha() != True:
            print("Username must start with a letter!")
        elif reg_user.isalnum() == False:
            print("Username can only contain letters and numbers")
        else:
            break

    while True:
        reg_pass = input("\nEnter password: ")

        if len(reg_pass) < 6:
            print("Password must be at least 6 characters!")
        elif reg_pass.isdigit() == True or reg_pass.isalpha() == True:
            print("Password must contain letters and numbers!")
        else:
            break

    while True:
        reg_email = input("\n Enter email: ")
        reg_email = reg_email.lower()

        for lists in user_db.values():
            if lists[1] == reg_email:
                print("Email adress already exists!")
                break
            elif reg_email.count("@") != 1 or \
                 reg_email.count(".") == 0 or len(reg_email) < 10:
                print("Invalid email adress!")
                break

        else:
            break

    user_db[reg_user] = [reg_pass, reg_email]

    print(f"{reg_user} registered. You may login now.")

    print(user_db)

    option = input("""
Menu:
1. Register
2. login

Select menu option: """)

while option == "2":
    while True:
        username = input("Enter username: ")
        username = username.capitalize()

        if username not in user_db:
            print("No such username!")
        else:
            break

    while True:
        password = input("Enter password: ")

        if password != user_db[username][0]:
            print("Incorrect password!")
        else:
            break
    break

print(f"Welcome {username}.")
