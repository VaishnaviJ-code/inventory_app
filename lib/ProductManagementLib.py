from datetime import datetime
from dao.AbstractProductDao import ProductDaoService
from dao.ProductDaoImplem import ProductDaoImplementation
from models.product import Product



class ProductManagementLib:

    'handles CRUD logic'

    dao_service: ProductDaoService = ProductDaoImplementation()

    @staticmethod
    def display_all_products():

        products = ProductManagementLib.dao_service.display_all_products()

        for product in products:
            print(product)

    @staticmethod
    def insert_products():

        product = Product()

        product_name = input("Enter Product Name: ")
        product.set_product_name(product_name)

        unit_price = float(input("Enter Product Unit Price: "))
        product.set_unit_price(unit_price)

        category_id = int(input("Enter Category ID: "))
        product.set_category_id(category_id)
        m_date = input("Enter Manufacturing Date (DD/MM/YYYY): ")
        util_date = datetime.strptime(m_date, "%d/%m/%Y")
        conv_m_date = util_date.date()
        product.set_manufacture_date(conv_m_date)
        product.set_is_active(is_active="Y")

        if ProductManagementLib.dao_service.insert_products(product):
            print("Inserted successfully...")
        else:
            print("Something went wrong!!!")

    @staticmethod
    def update_product():

        search_id = int(input("Enter the Product ID for updating: "))

        # create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(search_id)

        if not product:
            print("Product not found!!!")
            return
        
        print(product)

        confirm = input("Do you want to edit this data? (Y/N) ")
        if confirm.lower() == 'y':
            product.set_product_name(input("Enter Product Name: "))
            product.set_unit_price(float(input("Enter the Unit Price: ")))

            #pass the object to dao update
            if ProductManagementLib.dao_service.update_product(product, search_id):
                print("Updated Successfully...")
            else:
                print("Something went wrong!!!")

    @staticmethod
    def disable_product():

        search_id = int(input("Enter Product ID to be searched for disabling: "))

        product = ProductManagementLib.dao_service.find_by_product_id(search_id)

        if not product:
            print("Product not found!!!")
            return
        
        print(product)

        confirm = input("Do you want to disable this product? (Y/N) ")
        if confirm.lower() == 'y':

            if ProductManagementLib.dao_service.disable_product(search_id):
                print("Disabled Successfully...")
            else:
                print("Something went wrong!!!")

    @staticmethod
    def search_by_product_id():

        search_id = int(input("Enter Product ID to be searched: "))

        product = ProductManagementLib.dao_service.find_by_product_id(search_id)

        if not product:
            print("Product not found!!!")
            return
        
        print(product)

    @staticmethod
    def apply_gst_to_product():
        search_id = int(input("Enter the Product ID to apply GST: "))
        gst_percentage = float(input("Enter GST percentage to apply: "))
        if ProductManagementLib.dao_service.apply_gst(search_id, gst_percentage):
            print(f"GST of {gst_percentage} applied to product ID {search_id}")
        else:
            print("Failed to apply GST!!!")