import os
import retail_item
import cashregister

def main():
    pass

def menu():
    # menu recieves no arguments
    # it prompts the user with options to either modify the inventory
    # or shop
    
    # initalize variables
    passwords = ["abcdef", "heisenburg"]
    choice = 3
    
    # print the menu
    print("Please choose from the options below:")
    print("To access the inventory control system, press 1.")
    print("To access the retail store, press 2.")
    
    # get choice
    while choice != 1 and choice != 2:
        try:
            choice = int(input("Enter your choice: "))
        except:
            choice = 3
    
    if choice == 1:
        password = input("Enter the inventory control password: ")
        
        if password not in passwords:
            print("Wrong password, returning to main.")
            return
        else:
            retail_item.inventory_menu()