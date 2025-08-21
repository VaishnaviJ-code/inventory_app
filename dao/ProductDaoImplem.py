from typing import List
from dao.AbstractProductDao import ProductDaoService
from db.db_connection import DBConnection
from models.product import Product



class ProductDaoImplementation(ProductDaoService):
    
    ''' implementation for abstract class ProductDaoService'''

    # SQL Queries
    DISPLAY_ALL = "SELECT * FROM products WHERE is_active = 'Y'"
    INSERT_PRODUCT = "INSERT INTO products(product_name, unit_price, category_id, manufacture_date, is_active) VALUES (%s, %s, %s, %s, %s)"
    FIND_BY_ID = "SELECT * FROM products WHERE product_id = %s"
    UPDATE_PRODUCT = "UPDATE products SET product_name = %s, unit_price = %s WHERE product_id = %s"
    DISABLE_PRODUCT = "UPDATE products SET is_active = 'N' WHERE product_id = %s"
    APPLY_GST = "CALL apply_gst_to_product(%s, %s)"

    def __init__(self):
        self.conn = DBConnection().get_connection()

    def insert_products(self, product:Product)->bool:

        try:
            cursor = self.conn.cursor() # create a cursor object
            cursor.execute(self.INSERT_PRODUCT, 
                           (product.get_product_name(), 
                           product.get_unit_price(), 
                           product.get_category_id(), 
                           product.get_manufacture_date(), 
                           product.get_is_active())
                        )
            self.conn.commit() # changes made permanent
            return cursor.rowcount == 1 # returns True
        
        except Exception as e:
            print("Error inserting products: ",e)
            return False
        
        finally:
            cursor.close()

    def display_all_products(self)->List[Product]:

        products = [] # to store the records from DB

        try:
            cursor = self.conn.cursor(dictionary=True) # returns data in dictionary format
            cursor.execute(self.DISPLAY_ALL) # fire the query
            rows = cursor.fetchall()
            for row in rows:
                products.append(Product(product_id = row["product_id"],
                                        product_name = row["product_name"],
                                        unit_price = row["unit_price"],
                                        category_id = row["category_id"],
                                        manufacture_date = row["manufacture_date"],
                                        is_active = row["is_active"]))
        
        except Exception as e:
            print("Error fetching products: ", e)

        finally:
            cursor.close()

        return products # returns the list "products"
    
    def find_by_product_id(self, product_id:int):

        product = None

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FIND_BY_ID,(product_id,))
            row = cursor.fetchone()
            if row:
                product = Product(
                    product_id = row["product_id"],
                    product_name = row["product_name"],
                    unit_price = row["unit_price"],
                    category_id = row["category_id"],
                    manufacture_date = row["manufacture_date"],
                    is_active = row["is_active"]
                )

        except Exception as e:
            print("Error finding product ", e)

        finally:
            cursor.close()

        return product    
    def update_product(self, product:Product, product_id:int) -> bool:

        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.UPDATE_PRODUCT, 
                           (product.get_product_name(), 
                            product.get_unit_price(),
                            product_id)
                        )
            self.conn.commit()
            return cursor.rowcount == 1
        
        except Exception as e:
            print("Error Updating Product: ", e)
            return False
        
        finally:
            cursor.close()

    def disable_product(self, product_id:int) -> bool:
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.DISABLE_PRODUCT, 
                           (product_id,)
                        )
            self.conn.commit()
            return cursor.rowcount == 1
        
        except Exception as e:
            print("Error Disabling Product: ", e)
            return False
        
        finally:
            cursor.close()

    def apply_gst(self, product_id:int, gst_percetage:float) -> bool:
        cursor=None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.APPLY_GST,(product_id, gst_percetage))
            self.conn.commit()
            return cursor.rowcount >= 0 #since sp returns 0 if already applied gst
        except Exception as e:
            print("Error Applying GST: ", e)
        finally:
            if cursor:
                cursor.close()