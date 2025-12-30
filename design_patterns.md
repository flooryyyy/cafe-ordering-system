# Design Patterns

We used two main design patterns in this project to make the code cleaner and easier to expand later. Here's a quick explanation of what they are and why we used them.

## Factory Pattern
### What is it?
The Factory Pattern is basically a way to create objects without having to specify the exact class of the object that will be created. Instead of calling the constructor directly (like `FoodItem(...)`), we ask a factory to make it for us.

### Why did we use it?
It keeps all the creation logic in one place. If we want to add a new type of item later (like a "ComboMeal"), we just add it to the factory. We don't have to go through the whole code finding every place where we made a new item.

### Code Snippet
In `src/factory.py`, we check the type and create the right object:
```python
class MenuItemFactory:
    @staticmethod
    def create_item(item_type, name, price, **kwargs):
        if item_type == "food":
            return FoodItem(name, price, kwargs.get("vegetarian", False))
        elif item_type == "drink":
            return DrinkItem(name, price, kwargs.get("size", "medium"))
```
So in our main code, we just do:
```python
item = MenuItemFactory.create_item("food", "Burger", 5.00, vegetarian=False)
```

## Observer Pattern
### What is it?
The Observer Pattern defines a subscription mechanism. When one object (the subject) changes state, all its dependents (observers) are notified automatically.

### Why did we use it?
It's really useful for keeping the UI in sync with the data. When an item is added to an order, the Order object notifies anyone listening. This means if we added a display screen in the kitchen, it would automatically know when a new item was added without us having to change the `Order` class code.

### Code Snippet
In `src/order.py`, the Order class inherits from `OrderSubject`:
```python
class Order(OrderSubject):
    def add_item(self, item):
        self.menu_items.append(item)
        self.notify_observers()  # Tell everyone something changed!
```
Any class can "listen" by implementing an `update()` method and attaching itself to the order.
