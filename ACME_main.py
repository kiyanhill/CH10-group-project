import os
import retail_item
import cashregister
import pickle

def main():
    pass

def menu():
    # get the inventory
    file = open("inventory.dat", "rb")
    
    loaded_data = pickle.load(file)
    
    desc = loaded_data.get_description()
    units = loaded_data.get_units()
    price = float(loaded_data.get_price())
    
    print(f"{desc}")
    print(f"{units} units in stock")
    print(f"${price:.2f} for one")
    file.close()
    
    # get an item to buy
    