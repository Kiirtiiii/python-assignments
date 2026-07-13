# Assignment 4 : Customer Login Verification
correct_username = "admin"
correct_password = "python@123"
attempts = 0
 
while attempts < 3 :
    username = input("Enter Username:")
    password = input("Enter Password:")

    if username == correct_username and password == correct_password :
        print("\nLogin Successful")
        break
    else :
        attempts += 1
        print("Invalid Credentials")

        if attempts == 3 :
            print("Account Locked")
        else :
            print("Attempts Remaining:", 3 - attempts)