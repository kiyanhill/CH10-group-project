import os
import retail_item
import cashregister
import pickle

def main():
    pass
'''
def menu():
    # get the inventory
    items = {}
    with file = open("inventory.dat", "rb") as file:
        for line in file:
            # load a line
            loaded_data = pickle.load(file)

            # get the name, units, and price
            desc = loaded_data.get_description()
            units = loaded_data.get_units()
            price = float(loaded_data.get_price())

            # add the object to a dictionary with the name being the key

            items[desc] = loaded_data

            # print it for the viewer to see
            print(f"{desc}")
            print(f"{units} units in stock")
            print(f"${price:.2f} for one")

    # create the users cart
    cart = cashregister.CashRegister()

    # get an item to buy
    item = input("What item would you like to purchase?\n:>")

    while item not in items:
        item = input("What item would you like to purchase?\n:>")

    # set the users selected
    selected = items[item]

    #prime loop
    amount = -1

    while amount > selected.get_units() or amount <= 0:
        try:
            amount = int(input(f"How many {item}s would you like to buy?\n:>")
            # validate
            if amount <= 0:
                print("Bad number, please use a number greater than 0.")
            else:
                print("Too many requested, not enough stock.")
        except:
            # exception
            amount = amount
'''
def menu():
    # menu recieves no arguments
    # it prints out the users menu

    # iniitalize variables
    choice = -1
    choices = [1,2,3,4,5,6]
    register = cashregister.CashRegister()
    
    # print the menu
    print("Welcome to the ACME PoS retail system\nPlease choose from the following options:")
    print("\t1 - View Cart\n\t2 - Display items for sale\n\t3 - Purchase Item\n\t 4 - Empty cart and start over\n\t5 - Check out\n\t 6- EXIT to main")

    while choice not in choices:
        try:
            choice = int(input("Please enter a selection: "))
        except:
            pass

    if choice == 1:
        view_cart(register)

def view_cart(register):
    # view cart recieves an argument for the users cart
    # it prints all items in it

    # initialize the cart
    cart = register.get_cart()
    if cart == []:
        print("\nYour cart is empty!\n")   
        return

    for item in cart:
        print(f"\nDescription: {item.get_description}")
        print(f"Units: {item.get_units()}")
        print(f"Retail Price: ${item.get_price()}")

def items_for_sale():
    # items for sale recieves no arguments
    # it reads through inventroy to print all items currently for sale
    
    

    
