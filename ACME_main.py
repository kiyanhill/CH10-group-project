import os
import retail_item
import cashregister
import pickle

def main():
    pass

def menu():
    # menu recieves no arguments
    # it prints out the users menu

    # check if the inventory file exists
    if not os.path.exists("inventory.dat"):
        print("No inventory found. Add items to the inventory from the inventory control system.")
        return
    
    # iniitalize variables
    choice = -1
    choices = [1,2,3,4,5,6]
    register = cashregister.CashRegister()
    
    while choice != 6:
        # print the menu
        print("\nWelcome to the ACME PoS retail system\nPlease choose from the following options:")
        print("\t1 - View Cart\n\t2 - Display items for sale\n\t3 - Purchase Item\n\t 4 - Empty cart and start over\n\t5 - Check out\n\t 6- EXIT to main")

        while choice not in choices:
            try:
                choice = int(input("Please enter a selection: "))
            except:
                pass
        
        if choice == 1:
            view_cart(register)
            choice = -1
        elif choice == 2:
            t = items_for_sale()
            if t == False:
                choice = 6
            else:
                choice = -1
        elif choice == 3:
            t = purchase_item(register)
            if t == False:
                choice = 6
            else:
                choice = -1
        elif choice == 4:
            empty_cart(register)
            choice = -1
        elif choice == 5:
            check_out(register)
            choice = -1
        else:
            print("Thank you for using the ACME PoS retail system, goodbye.")
        

def view_cart(register):
    # view cart recieves an argument for the users cart
    # it prints all items in it

    # initialize the cart
    cart = register.get_cart()
    
    if cart == []:
        print("\nYour cart is empty!\n")   
        return

    for item in cart:
        print(f"\nDescription: {item.get_description()}")
        print(f"Units: {item.get_units()}")
        print(f"Retail Price: ${item.get_price()}")

def items_for_sale():
    # items for sale recieves no arguments
    # it reads through inventroy to print all items currently for sale
        
    with open("inventory.dat", "rb") as file:
        data = pickle.load(file)
        if data == None:
            print("No items found.")
            return False
        print(f"\nDescription: {data.get_description()}")
        print(f"Units: {data.get_units()}")
        print(f"Retail Price: ${data.get_price()}")

def purchase_item(register):
    # purchase item recieves an argument for the register
    # it adds an item to the cart and
    # asks if they want to add another
    
    # initialize the items
    items = {}
    
    # load all of the items for sale
    with open("inventory.dat", "rb") as file:
        item = pickle.load(file)
        if item == None:
            print("No items found.")
            return False
        print(f"\nDescription: {item.get_description()}")
        print(f"Units: {item.get_units()}")
        print(f"Retail Price: ${item.get_price()}")
        
        items[item.get_description()] = item
        
    # initialize the loop
    selected = False
    
    # get their item they want to buy
    while selected == False:
        item = input("What item would you like to purchase?\n:>")
        if item in items:
            selected = True
    
    # get the items object
    item = items[item]

    # initialize the loop
    amount = False
    
    # get the amount of the item
    while amount == False:
        try:
            amnt = int(input("How many would you like to purchase?\n:>"))
            if amnt > int(item.get_units()):
                print("Too many items requested, not enough stock.")
            elif amnt <= 0:
                print("Too little items selected, please selected 1 or more.")
            else:
                amount = True
        except:
            pass
                
    # add it to the register
#    oldunits = item.get_units()
#    item.set_units(int(oldunits) - amnt)
    item.set_units(amnt)
    register.purchase_item(item)
    
        
def empty_cart(register):
    # empty cart recieves an argument for the cash register
    # object and
    # it clears the cart and returns
    register.empty()

def check_out(register):
    # check out accepts an argument for the register
    total = register.get_total()
    cart = register.get_cart()
    for item in cart:
        print(f"\n{item.get_units()} {item.get_description()} <--> ${int(item.get_units()) * float(item.get_price()):.2f}")
    
    print(f"\nYour total is ${register.get_total():.2f}")
    print("Press Y to complete the transaction, anything else to empty the cart and return to the main.")
    
    choice = input(":>")
    if choice.lower() == "y":
        modify(cart)
    else:
        empty_cart(register)
    
def modify(items):
    # open the files
    file = open("inventory.dat", "rb")
    t_file = open("inventory_temp.dat", "wb")
    
    # read each item and check if the descriptions match
    for item in items:
        data = pickle.load(file)
        
        # change the amount
        if item.get_description() == data.get_description():
            amount = int(data.get_units()) - int(item.get_units())
            item.set_units(amount)
            
            # write
            pickle.dump(item, t_file)
        else:
            # write
            pickle.dump(data, t_file)
    
    # close the files
    file.close()
    t_file.close()
    # rename them
    os.remove("inventory.dat")
    os.rename("inventory_temp.dat", "inventory.dat")
        
menu()