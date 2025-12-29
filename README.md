# Café Digital Ordering System

A modular ordering system for a local café, built using object-oriented principles in Python.

## How to Run

1. Make sure you have Python 3 installed
2. Navigate to the project folder
3. Run the tests: `python3 src/tests.py`
4. Run the menu demo: `python3 src/menu.py`

## Features

- **Menu Management**: Add/remove food and drink items, load menu from JSON
- **Order Processing**: Create orders, add/remove items, calculate totals with VAT
- **Bill Generation**: Generate text-based receipts with itemised costs
- **Design Patterns**: Factory Pattern for item creation, Observer Pattern for order updates

## File Structure

```
src/
├── menu.py        # Menu, MenuItem, FoodItem, DrinkItem classes
├── menu.json      # Sample menu data
├── order.py       # Order class with observer pattern
├── bill.py        # Bill generation class
├── factory.py     # Factory pattern for creating menu items
├── observer.py    # Observer pattern base classes
└── tests.py       # Unit tests for all components
```

## Running Tests

```bash
python3 src/tests.py
```

All 9 tests should pass, covering:
- Menu item creation and details
- Order calculations (subtotal, VAT, total)
- Menu add/remove operations
- Bill generation
- Factory pattern
- Observer pattern notifications
- Error handling (empty orders, invalid inputs, negative prices)
