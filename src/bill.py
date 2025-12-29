# bill class - generates a receipt from an order
class Bill:
    def __init__(self, order):
        self.order = order
    
    # generate the receipt as a string
    def generate(self):
        # check if order is empty - can't generate bill for nothing
        if len(self.order.menu_items) == 0:
            raise ValueError("Cannot generate bill for empty order")
        
        # build the receipt line by line
        receipt = []
        receipt.append("=" * 30)
        receipt.append("        LOCAL CAFE RECEIPT")
        
        # add customer info if it exists
        if self.order.customer:
            receipt.append(f"Customer: {self.order.customer.name}")
            
        receipt.append("=" * 30)
        
        # add each item with its price
        for item in self.order.menu_items:
            # Pad name to 20 chars for alignment
            receipt.append(f"{item.name:<20} £{item.price:.2f}")
        receipt.append("-" * 30)
        receipt.append(f"{'Subtotal:':<20} £{self.order.get_total():.2f}")
        receipt.append(f"{'VAT (20%):':<20} £{self.order.get_vat():.2f}")
        receipt.append("-" * 30)
        receipt.append(f"{'TOTAL:':<20} £{self.order.get_total_cost():.2f}")
        receipt.append("=" * 30)
        receipt.append("      Thank you for purchasing from our local cafe!")
        
        # join all lines with newlines and return
        return "\n".join(receipt)
    
    # print the bill to the console
    def print_bill(self):
        print(self.generate())
