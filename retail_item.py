#retail item

class RetailItem:
    #manages inventory
    #have the following attributes
#     item description
#     units in inventory
#     price per unit
    def __init__(self,description,units,price):
        self.description=description
        self.units=units
        self.price=price
        
        
    def get_description(self):
        #you return the description
        return self.description
    
    def get_units(self):
        return self.units
    
    def get_price(self):
        return self.price
    
    