from menu import load_menu
from order import Order
from bill import Bill
from factory import MenuItemFactory
from customer import Customer

# helper to enforce valid choices
def get_valid_input(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print("Invalid choice, please try again.")

def run_cafe():
    print("--- WELCOME TO THE CAFE ---")
    
    # load menu at startup
    menu = load_menu()
    current_customer = None
    current_order = None
    
    # main app loop
    while True:
        print("\n--- MAIN MENU ---")
        if current_customer:
            print(f"Customer: {current_customer.get_details()}")
        print("1. Customer Management (Register/Login)")
        print("2. Menu Management (View/Add/Remove Items)")
        print("3. Order Management (New Order/Add Items)")
        print("4. Checkout & Pay")
        print("5. Exit")
        
        choice = input("Enter number: ")
        
        # Customer Management
        if choice == "1":
            print("\n--- CUSTOMER MANAGEMENT ---")
            name = input("Enter customer name: ")
            email = input("Enter email (optional, press enter to skip): ")
            try:
                current_customer = Customer(name, email if email else None)
                print(f"Welcome, {current_customer.name}!")
                # link pending order if it exists
                if current_order:
                    current_order.customer = current_customer
            except ValueError as e:
                print(f"Error: {e}")

        # Menu Management
        elif choice == "2":
            while True:
                print("\n--- MENU MANAGEMENT ---")
                print("1. View Menu")
                print("2. Add New Item")
                print("3. Remove Item")
                print("4. Back to Main Menu")
                
                menu_choice = input("Enter number: ")
                
                if menu_choice == "1":
                    menu.get_items()
                
                elif menu_choice == "2":
                    print("\nAdding new item...")
                    item_type = get_valid_input("Type (food/drink): ", ["food", "drink"])
                    name = input("Name: ")
                    try:
                        price = float(input("Price: "))
                        
                        if item_type == "food":
                            is_veg = input("Is vegetarian? (y/n): ").lower() == 'y'
                            item = MenuItemFactory.create_item("food", name, price, vegetarian=is_veg)
                        else:
                            size = input("Size (small/medium/large): ")
                            item = MenuItemFactory.create_item("drink", name, price, size=size)
                            
                        menu.add_item(item)
                        print(f"{name} added to menu!")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                elif menu_choice == "3":
                    name = input("Enter name of item to remove: ")
                    # look up item by name
                    items_to_remove = [item for item in menu.items if item.name.lower() == name.lower()]
                    
                    if items_to_remove:
                        for item in items_to_remove:
                            menu.remove_item(item)
                        print(f"Removed {len(items_to_remove)} items named '{name}'")
                    else:
                        print("Item not found.")
                        
                elif menu_choice == "4":
                    break

        # Order Management
        elif choice == "3":
            if not current_order:
                current_order = Order(current_customer)
                print("Created new order.")
            
            while True:
                print("\n--- ORDER MANAGEMENT ---")
                print("1. View Menu")
                print("2. Add Item to Order")
                print("3. View Current Order")
                print("4. Back to Main Menu")
                
                order_choice = input("Enter number: ")
                
                if order_choice == "1":
                    menu.get_items()
                elif order_choice == "2":
                    # find item and add it
                    name = input("Enter item name: ")
                    found = False
                    for item in menu.items:
                        if item.name.lower() == name.lower():
                            current_order.add_item(item)
                            print(f"Added {item.name}")
                            found = True
                            break
                    if not found:
                        print("Item not found in menu.")
                elif order_choice == "3":
                    if len(current_order.menu_items) == 0:
                        print("Order is empty.")
                    else:
                        current_order.get_items()
                        print(f"Total: £{current_order.get_total_cost():.2f}")
                elif order_choice == "4":
                    break

        # Checkout
        elif choice == "4":
            if not current_order or len(current_order.menu_items) == 0:
                print("No active order to checkout.")
            else:
                try:
                    # generate receipt
                    bill = Bill(current_order)
                    print("\n" + bill.generate())
                    current_order = None
                    print("\nOrder completed and paid.")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_cafe()
