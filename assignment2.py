# Assignment 2 : ATM Withdrawal Simulator
# Taking input

account_holder = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance: "))

# allow upto 3 withdrawal attempts
for attempt in range(3) :
    withdrawal = float(input("Enter Withdrawal Amount: "))
    if withdrawal <= 0:
        print("Error : Withdrawal amount must be positive.")

    elif withdrawal > balance :
        print("Error : Insufficient Balance.")

    else :
        balance = balance -  withdrawal

        print("\n  Transaction Successful!  ")
        print("Account Holder :", account_holder)
        print("Withdrawal Amount:", withdrawal)
        print("Remaining Balance:", balance)
        break
else:
    print("\nTransaction Failed after 3 attempts.")
  