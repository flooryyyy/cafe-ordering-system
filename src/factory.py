from menu import FoodItem, DrinkItem

class MenuItemFactory:
    # Create items based on type
    @staticmethod
    def create_item(item_type, name, price, **kwargs):
        if item_type == "food":
            vegetarian = kwargs.get("vegetarian", False)
            return FoodItem(name, price, vegetarian)
        elif item_type == "drink":
            size = kwargs.get("size", "medium") 
            return DrinkItem(name, price, size)
        else:
            raise ValueError(f"Unknown item type: {item_type}")
