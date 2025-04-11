from database import init_db
from models import add_product,record_stock_movement,get_inventory

def run():
    init_db()
    while True:
        print("\nOptions: 1- Add Product  2- Record Stock Movement  3- View Inventory  4- Exit")
        choice=input("Enter choice: ")

        if choice == '1':
            name=input("Enter product name: ")
            sku=input("Enter SKU: ")
            add_product(name,sku)
        elif choice == '2':
            sku=input("Enter SKU: ")
            movement=input("Type (stock_in/sale/manual_removal): ")
            qty=int(input("Quantity: "))
            record_stock_movement(sku,movement, qty)
        elif choice == '3':
            inventory=get_inventory()
            for row in inventory:
                print(f"Product: {row[0]},SKU: {row[1]},Quantity: {row[2]}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()

