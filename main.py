# Super Cashier
import random
from datetime import datetime
import transaction

# Welcoming sign for customer
print("   ---Welcome to Supermarket Andi---   ")

# Input customer's name
nama = input("Enter Your Name : ")
if nama.isalpha(): 
    pass
else: 
# Condition if user input wrong type of text
    print("Invalid input. Please enter your name.")

# Generate transaction id for customer
trans_id = "TIK" + str(random.randint(1000, 9999))

# Show current date and time
current_date = datetime.now()
date = current_date.strftime("%d/%m/%Y ; %H:%M:%S")

# Printing all customer's info
print("---CUSTOMER---")
print(f"Name : {nama}")
print(f"Date : {date}")
print(f"Trans ID : {trans_id}")

# Ask user to add Items to their receipt
print("---Add Your Items---")
while True:
    transaction.add_item() #
    more_item = input("Do you want to add more items? (Y/N)").lower()
    if more_item == "n":
        break

while True:
    print("   ---Menu---   ")
    print("1. Add item to your cart")
    print("2. Update your item")
    print("3. Delete your item")
    print("4. Show my cart")
    print("5. Empty your cart")
    print("6. Checkout and Payment")
    print("7. Exit")

    try:
        choose = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid. Please choose a number.")
        continue

    if choose == 1:
        transaction.add_item()
        more_item = input("Do you want to add more items? (Y/N) ").lower()
        if more_item == "n":
            break
    
    elif choose == 2:
        update_menu = True
        while update_menu:
            print("1. Update item name")
            print("2. Update item quantity")
            print("3. Update price")
            print("4. Back to menu")

            try:
                update_choose = int(input("Enter your choice : "))
            except ValueError:
                print("Invalid. Please choose a number")
                continue

            if update_choose == 1:
                print("Updated Your Items")
                transaction.update_item()

            elif update_choose == 2:
                print("Updated Your Items")
                transaction.update_qt()

            elif update_choose == 3:
                print("Updated Your Items")
                transaction.update_price()

            elif update_choose == 4:
                update_menu = False

            else:
                print("Invalid. Please choose a number")

    elif choose == 3:
        delete_menu= True
        while delete_menu:
            print("1. Delete an item")
            print("2. Back to menu")

            try:
                delete_choose = int(input("Enter your choice : "))
            except ValueError:
                print("Invalid. Please choose a number")
                continue

            if delete_choose == 1:
                print("Updated Your Items")
                transaction.delete_item()

            elif delete_choose == 2:
                delete_menu = False

            else:
                print("Invalid. Please choose a number")

    elif choose == 4:
        print("My Cart")
        transaction.show_item()
    
    elif choose == 5:
        print("   ---CART EMPTY---   ")
        transaction.reset_item()

    elif choose == 6:
        payment_menu = True
        while payment_menu:
            print("Total Amount to Pay")
            transaction.payment_price()

    elif choose == 7:
        exit_menu = True
        while exit_menu:
            print("Exit Menu")
            print ("1. Yes")
            print("2. No")
            
            try:
                exit_choose = int(input("Are you sure? "))
            except ValueError:
                print("Please enter the correct number")
            
            if exit_choose == 1:
                print("Thank You for Choosing Us!")
                print("See You Again!")
                exit()

            elif exit_choose == 2:
                exit_menu = False

            else:
                print("Invalid.")
                print("Please input correct number")

    else:
        print("Please input correct number")
        


