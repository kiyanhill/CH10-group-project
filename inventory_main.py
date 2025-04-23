#main
import pickle
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
    print(item.get_description())
    return item

def write(item):
    #write the inventory to the file
    filename='inventory.dat'
    with open(filename,'wb') as file:
        pickle.dump(item,file)

def display():
    #just print the data had from the write file
    #read the file inventory . dat
    file=open('inventory.dat','rb')
    data=pickle.load(file)
    item=data.get_description()
    unit=data.get_units()

def inventory_menu():
    
    going='y'
    while going=='y':
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
            item=add_inventory()
        elif choice==2:
            display()
        elif choice==3:
            write(item)
        else:
            main_menu()
            print("Please only make a valid choice form from the menu")
        going=input("Do you want to keep going? (y/n) :")
        if going=="n":
            main_menu()