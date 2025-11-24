# 3
# Create a program using functions for banking applications where a user can 
# deposit amount, withdraw amount, and check balance.  

balance = 0.0

def deposite(amount):
    global balance

    if amount > 0: 
        balance += amount
        print("deposite successfully")
    else :
        print("failed")

def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient balcance ")
    elif  amount <= 0:
        print("invalid amount Entered")
    else: 
        balance -= amount
        print("Amount withdraw")

def check_balance():
   print("Balance is : ", balance)

while True:
       print("1-Deposite\n2-Withdraw\n3-Check balance\nExit")

       choice = input("\nEnter your choice") 

       if choice == '1':
           amt = float(input("enter amount to deposite :"))
           deposite(amt)
        
       elif choice == '2':
           amt = float(input("Enter the amount to withdraw"))
           withdraw(amt)
           
       elif choice == '3':
            check_balance()

       elif choice == '4':
           print("Exit")
           break
       
       else :
           print("Invalid choice")
             
# 3
# Create a program using functions for banking applications where a user can 
# deposit amount, withdraw amount, and check balance.  

# balance = 0.0

# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#         print("Deposit successful!")
#     else:
#         print("Deposit failed. Enter a valid amount.")

# def withdraw(amount):
#     global balance
#     if amount > balance:
#         print("Insufficient balance!")
#     elif amount <= 0:
#         print("Invalid amount entered!")
#     else:
#         balance -= amount
#         print("Withdrawal successful!")

# def check_balance():
#     print("Current Balance:", balance)

# # Main program
# while True:
#     print("\n--- Banking Menu ---")
#     print("1 - Deposit")
#     print("2 - Withdraw")
#     print("3 - Check Balance")
#     print("4 - Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         amt = float(input("Enter amount to deposit: "))
#         deposit(amt)
#     elif choice == '2':
#         amt = float(input("Enter amount to withdraw: "))
#         withdraw(amt)
#     elif choice == '3':
#         check_balance()
#     elif choice == '4':
#         print("Thank you for using our banking system!")
#         break
#     else:
#         print("Invalid choice! Please try again.")
