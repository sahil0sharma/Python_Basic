# -------------8---------
# Design a menu-driven Python program for a Grocery Store Inventory System. The 
# program should allow the user to perform the following operations:  
# 1.   Add an item to the inventory 
# 2.   Remove an item from the inventory 
# 3.   View all items in the inventory 
# 4.   Check quantity of a specific item 
# Use appropriate functions for each operation. The program should keep running 
# until the user chooses to exit 

Inventory  = {}

def add():
    item = input("Enter the item name : ")
    qty = int(input("Enter the quantity you want : "))

    if item in Inventory:
        Inventory[item] = Inventory[item] + qty
    else :
        Inventory[item] = qty
        print(f"{item}(s) added.")

def remove():
    item = input("Enter the item name : ")
    if item in Inventory:
        del Inventory[item]
        print(f"{item} Removed")
    else :
        print("Item not found")

def display():
    if not Inventory:
        print("INventory is empty ")
    else: 
        for item , qty in Inventory.items():
            print(f"{item} in {qty}")
def check():
    item = input("Enter the item name : ")
    if item in Inventory:
        print("item is present ")
    else: 
        print("wrong choice")


while True:
    print("\n--- Grocery Store Inventory Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View All Items")
    print("4. Check Quantity")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add()
    elif choice == '2':
        remove()
    elif choice == '3':
        display()
    elif choice == '4':
        check()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")

    