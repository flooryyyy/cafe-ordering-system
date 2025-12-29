# Testing Report

## Test Summary

| Test | Status |
|------|--------|
| test_food_item | ✓ PASS |
| test_order_calculations | ✓ PASS |
| test_menu_management | ✓ PASS |
| test_bill_generation | ✓ PASS |
| test_factory_pattern | ✓ PASS |
| test_observer_pattern | ✓ PASS |
| test_empty_order_error | ✓ PASS |
| test_invalid_item_name | ✓ PASS |
| test_negative_price | ✓ PASS |

**Total: 9 tests, 9 passed, 0 failed**

## Test Coverage

### Core Functionality
- **MenuItem**: Tests that FoodItem stores name, price, and vegetarian status correctly
- **Order**: Tests add_item, get_total, get_vat, and get_total_cost calculations
- **Menu**: Tests add_item and remove_item operations
- **Bill**: Tests that receipt contains correct items and totals

### Design Patterns
- **Factory**: Tests that create_item returns correct types (FoodItem/DrinkItem)
- **Observer**: Tests that observers receive notifications when items are added

### Error Handling
- **Empty Order**: Verifies ValueError is raised when generating bill for empty order
- **Invalid Name**: Verifies ValueError for empty item name
- **Negative Price**: Verifies ValueError for negative prices

## How to Run Tests

```bash
cd /path/to/project
python3 src/tests.py
```

Expected output:
```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```
