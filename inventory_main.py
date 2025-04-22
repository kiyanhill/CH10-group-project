#main

import retail_item as r

def add_inventory():
    #get input from user of item inventory and price
    
    desc=input("Enter your item: ")
    #desc=r.RetailItem(desc)
    
    item_units=input("Enter how many you want: ")
    #item_unit=RetailItem(item_unit)
    
    item_price=input("Enter your price: ")
    #item_price=RetailItem(item_price)
    item=r.RetailItem(desc,item_units,item_price)
    
def write():
    pass
def inventory_menu():
    pass

def display():
    pass

def inventory_menu():
    
    choice=0
    
    #output the menu to user
    print("Choose a program from the following options")
    print("1: add inventory")
    print("2: view inventory")
    print("3: write inventory")
    print("4: end")
    
    
    #get input for the user choice
    choice= int(input(":>"))
    
    #process the menu
    if choice==1:
        add_inventory()
    elif choice==2:
        display()
    elif choice==3:
        write()
    else:
        main_menu()