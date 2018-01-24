# name: Erich Ostendarp
# date: 9/30/2017
# purpose: A single person ATM that allows one person with a predetermined ID and password to access their money.

ID = "admin"
PASSWORD = "password"
balance = 100

while True:
    user_id = input("Enter ID: ")
    user_password = input("Enter password: ")

    logged_in = False

    while not logged_in:
        if user_id != ID and user_password != PASSWORD:
            print("Login Failed")
            user_id = input("Enter ID: ")
            user_password = input("Enter password: ")
        else:
            logged_in = True

    while logged_in:
        user_action = int(input("Enter \'1\' for withdrawal or \'2\' for deposit or"
                                " \'3\' to check their balance or \'4\' to logout: "))

        if user_action == 1:
            withdrawal_amount = int(input("Enter withdrawal amount: "))
            balance -= withdrawal_amount
            print("withdrawal amount: " + str(withdrawal_amount) + " balance: " + str(balance))
        elif user_action == 2:
            deposit_amount = int(input("Enter deposit amount: "))
            balance += deposit_amount
            print("deposit amount: " + str(deposit_amount) + " balance: " + str(balance))
        elif user_action == 3:
            print("Balance: " + str(balance))
        else:
            print("Logged out")
            logged_in = False
