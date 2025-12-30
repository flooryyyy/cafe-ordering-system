# load menu data from the json file
from menu import load_menu
# order class to manage what people want to buy
from order import Order
# bill class to print receipts later
from bill import Bill
# factory to easily create food or drink items
from factory import MenuItemFactory
# customer to handle user details
from customer import Customer

# better UI 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

# initialize global console
console = Console()

# helper function to validate user inputs
def get_valid_input(prompt, options):
    # runs until we get a valid answer
    while True:
        # ask the user for input using rich prompt
        choice = Prompt.ask(prompt, choices=options)
        return choice

# create a table for the main menu using "rich" library
def create_menu_table():
    table = Table(title="Main Menu", show_header=True, header_style="bold purple")
    table.add_column("No.", style="cyan", width=2)
    table.add_column("Option", style="yellow")
    
    table.add_row("1", "Login or Register")
    table.add_row("2", "View/Add/Remove Items")
    table.add_row("3", "Add Items to Order")
    table.add_row("4", "Checkout & Pay")
    table.add_row("5", "Exit")
    return table

def run_cafe():
    console.print(Panel.fit("☕ WELCOME TO THE CAFE ☕", style="bold yellow"))
    
    # load menu at startup
    menu = load_menu()
    current_customer = None
    current_order = None
    
    # main app loop
    while True:
        console.print() # spacer
        # if current_customer:
        #     console.print(f"[bold green]Customer: {current_customer.get_details()}[/]")
        
        # Display main menu table
        table = Table(title="Currently Logged In: " + (f"[green]{current_customer.name}[/]" if current_customer else "[red]Guest[/]"))
        table.add_column("Option", justify="right", style="cyan", no_wrap=True)
        table.add_column("Description", style="white")

        table.add_row("1", "Login or Register")
        table.add_row("2", "Manage Menu (Admin)")
        table.add_row("3", "Place Order")
        table.add_row("4", "Checkout")
        table.add_row("5", "Exit")
        
        console.print(table)
        
        choice = Prompt.ask("Enter number", choices=["1", "2", "3", "4", "5"])
        
        # Customer Management
        if choice == "1":
            console.print(Panel("[bold]CUSTOMER MANAGEMENT[/]", style="blue"))
            name = console.input("Enter customer name: ")
            email = console.input("Enter email (optional): ")
            try:
                current_customer = Customer(name, email if email else None)
                console.print(f"[bold green]Welcome, {current_customer.name}![/]")
                # link pending order if it exists
                if current_order:
                    current_order.customer = current_customer
            except ValueError as e:
                console.print(f"[red]Error: {e}[/]")

        # Menu Management
        elif choice == "2":
            while True:
                console.print("\n[bold]MENU MANAGEMENT[/]")
                console.print("1. View Menu")
                console.print("2. Add New Item")
                console.print("3. Remove Item")
                console.print("4. Back")
                
                menu_choice = Prompt.ask("Choose", choices=["1", "2", "3", "4"])
                
                if menu_choice == "1":
                    # We can also upgrade this to a table, but for now just print nicely
                    console.print("[bold underline]Current Menu:[/]")
                    menu_table = Table(show_header=True, header_style="bold magenta")
                    menu_table.add_column("Type", style="cyan")
                    menu_table.add_column("Name", style="white")
                    menu_table.add_column("Price", justify="right", style="green")
                    
                    for item in menu.items:
                        import inspect
                        # hacky type check or just string check
                        itype = "Drink" if hasattr(item, 'size') else "Food"
                        menu_table.add_row(itype, item.name, f"£{item.price:.2f}")
                    console.print(menu_table)
                
                elif menu_choice == "2":
                    console.print("[yellow]Adding new item...[/]")
                    item_type = get_valid_input("Type", ["food", "drink"])
                    name = console.input("Name: ")
                    try:
                        price = float(console.input("Price: "))
                        
                        if item_type == "food":
                            is_veg = Confirm.ask("Is vegetarian?")
                            item = MenuItemFactory.create_item("food", name, price, vegetarian=is_veg)
                        else:
                            size = Prompt.ask("Size", choices=["small", "medium", "large"])
                            item = MenuItemFactory.create_item("drink", name, price, size=size)
                            
                        menu.add_item(item)
                        console.print(f"[bold green]{name} added to menu![/]")
                    except ValueError as e:
                        console.print(f"[bold red]Error: {e}[/]")
                
                elif menu_choice == "3":
                    name = console.input("Enter name of item to remove: ")
                    items_to_remove = [item for item in menu.items if item.name.lower() == name.lower()]
                    
                    if items_to_remove:
                        for item in items_to_remove:
                            menu.remove_item(item)
                        console.print(f"[green]Removed {len(items_to_remove)} items named '{name}'[/]")
                    else:
                        console.print("[red]Item not found.[/]")
                        
                elif menu_choice == "4":
                    break

        # Order Management
        elif choice == "3":
            if not current_order:
                current_order = Order(current_customer)
                console.print("[dim]Created new order.[/]")
            
            while True:
                console.print("\n[bold]ORDER MANAGEMENT[/]")
                console.print("1. View Menu")
                console.print("2. Add Item")
                console.print("3. View Cart")
                console.print("4. Back")
                
                order_choice = Prompt.ask("Choose", choices=["1", "2", "3", "4"])
                
                if order_choice == "1":
                    # Duplicate logic for now, or we could make a helper
                     # Simple list for speed
                     for item in menu.items:
                         console.print(f"- {item.name} (£{item.price})")
                elif order_choice == "2":
                    name = console.input("Item name: ")
                    found = False
                    for item in menu.items:
                        if item.name.lower() == name.lower():
                            current_order.add_item(item)
                            console.print(f"[bold green]Added {item.name}[/]")
                            found = True
                            break
                    if not found:
                        console.print("[red]Item not found.[/]")
                elif order_choice == "3":
                    if not current_order.menu_items:
                        console.print("[yellow]Order is empty.[/]")
                    else:
                        cart_table = Table(title="Your Cart")
                        cart_table.add_column("Item")
                        cart_table.add_column("Price", justify="right")
                        for item in current_order.menu_items:
                             cart_table.add_row(item.name, f"£{item.price:.2f}")
                        cart_table.add_row("---", "---")
                        cart_table.add_row("[bold]Total[/]", f"[bold]£{current_order.get_total_cost():.2f}[/]")
                        console.print(cart_table)
                elif order_choice == "4":
                    break

        # Checkout
        elif choice == "4":
            if not current_order or not current_order.menu_items:
                console.print("[red]No active order to checkout.[/]")
            else:
                try:
                    bill = Bill(current_order)
                    # bill.generate() now returns a rich Panel
                    console.print(bill.generate())
                    current_order = None
                    console.print("[bold green]Order completed and paid![/]")
                    console.input("[dim]Press Enter to continue...[/]")
                except ValueError as e:
                    console.print(f"[red]Error: {e}[/]")

        elif choice == "5":
            console.print("[bold yellow]Goodbye![/]")
            break
            
if __name__ == "__main__":
    run_cafe()
