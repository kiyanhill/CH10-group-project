class CashRegister():
    def __init__(self):
        self.__total = 0
        self.__cart = []
        
    def purchase_item(self, item):
        self.__cart.append(item)
        
    def get_total(self):
        for item in self.__cart:
            self.__total += item.get_price()
        return self.__total
    
    def get_cart(self):
        return self.__cart
    
    def empty(self):
        self.__cart = []
    