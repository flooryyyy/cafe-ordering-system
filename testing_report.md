# Testing Report Settings

For Task 4, I've written a suite of unit tests to ensure the system is robust and doesn't crash easily. The tests cover the main logic like calculating totals, managing the menu, and generating bills.

## What's Tested?

I focused on the critical parts of the application:

1.  **Core Logic**:
    *   **Calculations**: Verified that `get_total()` and `get_vat()` sums up correctly.
    *   **Menu**: Checked that we can add and remove items from the menu list.
    *   **Bill**: Ensured the bill generation runs without errors and pulls the right customer data.

2.  **Design Patterns**:
    *   **Factory**: Tested that asking for "food" actually gives us a `FoodItem` and "drink" gives a `DrinkItem`.
    *   **Observer**: Created a dummy observer to count how many times it gets notified when items are added to an order.

3.  **Error Handling**:
    *   **Empty Orders**: You can't checkout with an empty cart. The system raises a `ValueError` (which the UI catches).
    *   **Invalid Inputs**: Creating an item with a negative price or empty name raises a `ValueError`.

## Test Results

I ran the tests using Python's `unittest` framework. All 11 tests passed.

```
Ran 11 tests in 0.001s

OK
```

This gives me confidence that everything is working as it should.
