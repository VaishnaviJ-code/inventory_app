from lib.ProductManagementLib import ProductManagementLib

def main():

    while True:

        print("\n -------------------- PRODUCT MANAGEMENT ------------------")
        print("1. ADD PRODUCT")
        print("2. DISPLAY ALL PRODUCT")
        print("3. UPDATE PRODUCT")
        print("4. SEARCH PRODUCT")
        print("5. DISABLE PRODUCT")
        print("6. APPLY GST TO PRODUCT")
        print("7. EXIT")

        choice = input("\nEnter your choice from 1-6: ")
        if choice == "1":
            ProductManagementLib.insert_products()
        elif choice == "2":
            ProductManagementLib.display_all_products()
        elif choice == "3":
            ProductManagementLib.update_product()
        elif choice == "4":
            ProductManagementLib.search_by_product_id()
        elif choice == "5":
            ProductManagementLib.disable_product()
        elif choice == "6":
            ProductManagementLib.apply_gst_to_product()
        elif choice == "7":
            break

if __name__ == "__main__":
    main()