# bill class - generates a receipt from an order
class Bill:
    def __init__(self, order):
        self.order = order
    
    def generate(self):
        # prevent empty receipts
        if not self.order.menu_items:
            raise ValueError("Cannot generate bill for empty order")
        
        receipt = []
        receipt.append("=" * 30)
        receipt.append("        LOCAL CAFE RECEIPT")
        
        # add customer if available
        if self.order.customer:
            receipt.append(f"Customer: {self.order.customer.name}")
            
        receipt.append("=" * 30)
        
        # list items
        for item in self.order.menu_items:
            # push price to the right (column 20)
            receipt.append(f"{item.name:<20} £{item.price:.2f}")
        receipt.append("-" * 30)
        receipt.append(f"{'Subtotal:':<20} £{self.order.get_total():.2f}")
        receipt.append(f"{'VAT (20%):':<20} £{self.order.get_vat():.2f}")
        receipt.append("-" * 30)
        receipt.append(f"{'TOTAL:':<20} £{self.order.get_total_cost():.2f}")
        receipt.append("=" * 30)
        receipt.append("      Thank you for purchasing from our local cafe!")
        
        return "\n".join(receipt)
    
    def print_bill(self):
        print(self.generate())
