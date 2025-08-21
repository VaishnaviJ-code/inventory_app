from datetime import date
import re

class Product :
    '''
        Python OOPs applied
    '''
    def __init__(self, product_id = None, product_name = None,
                 unit_price = None, category_id = None,
                 manufacture_date = None,
                 is_active = "Y"):

        self.__product_id = product_id
        self.__product_name = product_name # validating productname
        self.__unit_price = unit_price
        self.__category_id = category_id
        self.__manufacture_date = manufacture_date if manufacture_date else date.today()
        self.__is_active = is_active
        
    # ---------------------
    # getters and setters
    # ---------------------

    def get_product_id(self):
        return self.__product_id
    
    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_product_name(self):
        return self.__product_name
    
    def set_product_name(self, product_name):

        'validate product name before setting (2-30 alphabets/underscore)'

        pattern = re.compile(r"^[A-Za-z_]{2,20}$")

        while True:
            if pattern.match(product_name):
                self.__product_name = product_name
                break
            else:
                print("\t\t Invalid product Name \n product name must have only alphabets and underscore \n  min character - 2 \nmax character - 20!!!")
                product_name = input("\t\t Enter Product Name again: ")

    def get_unit_price(self):
        return self.__unit_price
    
    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    def get_category_id(self):
        return self.__category_id
    
    def set_category_id(self, category_id):
        self.__category_id = category_id

    def get_manufacture_date(self):
        return self.__manufacture_date
    
    def set_manufacture_date(self, manufacture_date):
        if isinstance(manufacture_date, date):
            self.__manufacture_date = manufacture_date
        else:
            raise ValueError("manufacture date  must be date object")
        
    def get_is_active(self):
        return self.__is_active
    
    def set_is_active(self, is_active):
        self.__is_active = is_active
    
    #override __str__
    def __str__(self):
        return f"Product ID: {self.__product_id:<10}. Product name: {self.__product_name:<20}. Categoryid: {self.__category_id:<10}. Unit price: {self.__unit_price:<15}. Manufacturing Date: {self.__manufacture_date}. Is Active: {self.__is_active:<10}"
    