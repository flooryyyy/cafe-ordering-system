# Café Digital Ordering System

This is my project for the Advanced Programming assessment (Task 2). It's a digital ordering system for a local café that lets you manage the menu, take orders, and generating bills.

I built this using Python and tried to stick to Object-Oriented Programming (OOP) principles as much as possible.

## Key Features

Here's what the system can do right now:
*   **Menu Management**: You can add new food/drinks or remove them. It even loads the menu from a file (`menu.json`) so you don't have to type it in every time.
*   **Taking Orders**: You can create an order for a customer and add items to their cart.
*   **Bill Generation**: It calculates the total cost (including 20% VAT) and prints out a nice receipt.
*   **Customer Handling**: You can link orders to specific customers (name/email).
*   **Design Patterns**: I used the **Factory Pattern** to make creating items easier and the **Observer Pattern** so the system "knows" when an order changes.

## How to Run It

First, make sure you've got the dependencies installed (I used `rich` for the UI):
```bash
pip install rich
```

Then you can run the main app like this:
```bash
python3 src/interface.py
```

### Running Tests
I also wrote some unit tests to make sure I didn't break anything. You can run them with:
```bash
python3 tests/test_main.py
```
They should all pass (hopefully!).

## Project Structure
All the source code is in `src/`:
*   `interface.py`: The main program loop.
*   `menu.py`: Handles the menu logic.
*   `order.py`: Handles the cart/orders.
*   `bill.py`: Generates the receipt.

For more info on how I designed it:
*   [Design Patterns](design_patterns.md)
*   [Testing Report](testing_report.md)
