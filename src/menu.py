import json

# class to manage the menu
class Menu:
    def __init__(self):
        # list to hold all menu items
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    # print all items
    def get_items(self):
        for item in self.items:
            print(item.get_details())

# load data from json file
def load_menu():
    menu = Menu()
    try:
        # try to open the valid file
        with open("src/menu.json", "r") as file:
            menu_data = json.load(file)
            
        for item in menu_data:
            if item["type"] == "food":
                menu.add_item(FoodItem(item["name"], item["price"], item["vegetarian"]))
            elif item["type"] == "drink":
                menu.add_item(DrinkItem(item["name"], item["price"], item["size"]))
    except FileNotFoundError:
        # if file is missing, just start empty
        pass
    return menu

# base class for anything on the menu
class MenuItem:
    def __init__(self, name, price):
        # validation
        if not name or not isinstance(name, str):
            raise ValueError("Item name must be a non-empty string")
        if price < 0:
            raise ValueError("Item price must not be negative")
        
        self.name = name
        self.price = price
    
    def get_details(self):
        return f"{self.name} costs £{self.price:.2f}"

# specific food item class
class FoodItem(MenuItem):
    def __init__(self, name, price, vegetarian):
        super().__init__(name, price)
        self.vegetarian = vegetarian
    
    def get_details(self):
        details = super().get_details()
        return f"{details} (vegetarian)" if self.vegetarian else details

# specific drink item class
class DrinkItem(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price) 
        self.size = size
    
    def get_details(self):
        details = super().get_details()
        return f"{details} (size: {self.size})"

if __name__ == "__main__":
    menu = load_menu()
    menu.get_items()
