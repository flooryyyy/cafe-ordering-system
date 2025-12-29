# define a class for ordering
class Order:
    def __init__(self, items, observer):
        self.items = items
        self.observer = observer