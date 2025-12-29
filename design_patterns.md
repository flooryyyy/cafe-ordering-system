# Design Pattern Explanation

## Factory Pattern (factory.py)

### What It Does
The Factory Pattern creates MenuItem objects without exposing the creation logic. Instead of calling `FoodItem()` or `DrinkItem()` directly, you use `MenuItemFactory.create_item()`.

### Why We Chose It
1. **Scalability**: If we add new item types later (e.g., SpecialItem, ComboItem), we only need to update the factory, not all the code that creates items
2. **Consistency**: All items are created the same way, reducing bugs
3. **Flexibility**: The factory can add validation or default values in one place

### Code Example
```python
# Without factory - scattered code
food = FoodItem("Pizza", 8.00, True)
drink = DrinkItem("Tea", 1.50, "small")

# With factory - centralised creation
food = MenuItemFactory.create_item("food", "Pizza", 8.00, vegetarian=True)
drink = MenuItemFactory.create_item("drink", "Tea", 1.50, size="small")
```

---

## Observer Pattern (observer.py, order.py)

### What It Does
The Observer Pattern lets objects "subscribe" to changes in another object. When an Order changes (item added/removed), all subscribers are automatically notified.

### Why We Chose It
1. **Real-time Updates**: A display screen could update automatically when orders change
2. **Loose Coupling**: The Order class doesn't need to know what's listening - it just notifies
3. **Future Features**: Easy to add notifications to kitchen, mobile app, or stock system

### Code Example
```python
class KitchenDisplay(OrderObserver):
    def update(self, order):
        print(f"Kitchen: Order updated, {len(order.menu_items)} items")

order = Order()
display = KitchenDisplay()
order.add_observer(display)

order.add_item(burger)  # Kitchen display automatically notified
```

### How It Improves the System
- **Modularity**: New observers can be added without changing Order class
- **Maintainability**: Each observer handles its own logic
- **Scalability**: Supports multiple concurrent observers (display, printer, mobile app)
