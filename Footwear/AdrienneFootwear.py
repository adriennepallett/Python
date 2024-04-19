# Assignment 12 - Final Exam

class Footwear():
    def __init__(self,br,sz,de,wt,pr):
        self.__brand = br
        self.__size = sz
        self.__desc = de
        self.__weight = wt
        self.__price = pr
        self.__quantity = 1

    def get_brand(self):
        return self.__brand
    def get_size(self):
        return self.__size
    def get_desc(self):
        return self.__desc
    def get_weight(self):
        return self.__weight
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity

    def set_brand(self,br):
        self.__brand = br
    def set_size(self,sz):
        self.__size = sz
    def set_desc(self,de):
        self.__desc = de
    def set_weight(self,wt):
        self.__weight = wt
    def set_price(self,pr):
        self.__price = pr
    def set_quantity (self,q):
        self.__quantity = q

    def get_order_price(self):
        dTotalPrice = self.__quantity * self.__price
        return dTotalPrice
    
    def get_order_weight_in_ounces(self):
        iTotalWeight = self.__quantity * self.__weight
        return iTotalWeight
        
    def __str__(self):
        ret_str = str(self.__price) + " each for " + str(self.__quantity) + " "
        ret_str += str(self.__brand) + " " + str(self.__desc) + " of size " + str(self.__size)
        return ret_str
