
# bill class - generates a receipt from an order
from rich.table import Table
from rich.panel import Panel
from rich import box 

class Bill:
    def __init__(self, order):
        self.order = order
    
    def generate(self):
        # prevent empty receipts
        if not self.order.menu_items:
            raise ValueError("Cannot generate bill for empty order")
        
        # Create a table for the receipt content
        table = Table(box=None, show_header=False, expand=True, padding=(0, 1))
        table.add_column("Item", justify="left", ratio=3)
        table.add_column("Price", justify="right", ratio=1)
        
        # add customer if available
        if self.order.customer:
            table.add_row(f"[bold]Customer: {self.order.customer.name}[/]", "")
            table.add_section()
            
        # list items
        for item in self.order.menu_items:
            table.add_row(item.name, f"£{item.price:.2f}")
            
        table.add_section()
        table.add_row("Subtotal:", f"£{self.order.get_total():.2f}")
        table.add_row("VAT (20%):", f"£{self.order.get_vat():.2f}")
        
        # Final total with bold styling
        table.add_section()
        table.add_row("[bold]TOTAL:[/]", f"[bold]£{self.order.get_total_cost():.2f}[/]")
        
        # Return the table wrapped in a Panel
        return Panel(
            table, 
            title="🧾 LOCAL CAFE RECEIPT", 
            subtitle="Thank you for visiting!",
            border_style="blue",
            width=50
        )
    
    def print_bill(self):
        print(self.generate())

