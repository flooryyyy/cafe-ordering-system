from observer import OrderSubject

class Order(OrderSubject):
    def __init__(self, customer=None):
        super().__init__()
        self.menu_items = []
        self.customer = customer


    def add_item(self, item):
        self.menu_items.append(item)
        self.notify_observers()

    def remove_item(self, item):
        self.menu_items.remove(item)
        self.notify_observers()

    def get_items(self):
        for item in self.menu_items:
            print(item.get_details())

    def get_total(self):
        return sum(item.price for item in self.menu_items)

    def get_vat(self):
        return self.get_total() * 0.2

    def get_total_cost(self):
        return self.get_total() + self.get_vat()