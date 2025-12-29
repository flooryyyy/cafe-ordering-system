import json

# create a menu with an array to store the items
class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        for item in self.items:
            print(item.get_details())

# create a function to load the menu from menu.json
def load_menu():
    # create a menu object
    menu = Menu()
    # open the menu.json file
    with open("src/menu.json", "r") as file:
        menu_data = json.load(file)
    # loop through the menu items
    for item in menu_data:
        # if it's food, create a food item
        if item["type"] == "food":
            menu.add_item(FoodItem(item["name"], item["price"], item["vegetarian"])) # add the item to the menu
        # if it's a drink, create a drink item
        elif item["type"] == "drink":
            menu.add_item(DrinkItem(item["name"], item["price"], item["size"]))
    # return the menu once finished loading
    return menu

# create a menu item class
class MenuItem:
    # initialise the menu item with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # define a function to get details of an item
    def get_details(self):
        return f"{self.name} costs £{self.price:.2f}" # :.2f rounds to 2 decimal places (£3.4 --> £3.40)

# inherit from MenuItem
class FoodItem(MenuItem):
    # init with attributes
    def __init__(self, name, price, vegetarian):
        super().__init__(name, price) # super() calls the parent class
        # store unique attribute(s)
        self.vegetarian = vegetarian # true/false
    
    # define a function to get details of a food item
    def get_details(self):
        details = super().get_details() # call the parent class function and store it to reduce repetition
        return f"{details} (vegetarian)" if self.vegetarian else details # if vegetarian, add (vegetarian) to the end

class DrinkItem(MenuItem):
    # initialise menu item with name and price
    def __init__(self, name, price, size):
        # call parent class to create a MenuItem object
        super().__init__(name, price) 
        # store unique attribute(s)
        self.size = size # small, medium, large
    
    # define a function to get details of a drink
    def get_details(self):
        details = super().get_details() # store details
        return f"{details} (size: {self.size})" # add "size: small/medium/large" at the end

# load the menu from the json file
menu = load_menu()

# print the menu items
menu.get_items()

