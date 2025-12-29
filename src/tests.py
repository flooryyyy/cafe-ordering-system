import unittest
from menu import Menu, FoodItem, DrinkItem
from order import Order
from bill import Bill
from factory import MenuItemFactory
from observer import OrderObserver
from customer import Customer

class TestCafeSystem(unittest.TestCase):
    
    def test_food_item(self):
        burger = FoodItem("Burger", 5.00, False)
        self.assertEqual(burger.name, "Burger")
        self.assertEqual(burger.price, 5.00)
        self.assertEqual(burger.vegetarian, False)
        
    def test_order_calculations(self):
        order = Order()
        burger = FoodItem("Burger", 5.00, False)
        coke = DrinkItem("Coke", 2.00, "large")
        
        order.add_item(burger)
        order.add_item(coke)
        
        self.assertEqual(order.get_total(), 7.00)
        self.assertAlmostEqual(order.get_vat(), 1.40)
        self.assertAlmostEqual(order.get_total_cost(), 8.40)

    def test_menu_management(self):
        menu = Menu()
        item = FoodItem("Test", 1.00, True)
        
        menu.add_item(item)
        self.assertIn(item, menu.items)
        
        menu.remove_item(item)
        self.assertNotIn(item, menu.items)

    def test_bill_generation(self):
        order = Order()
        order.add_item(FoodItem("Burger", 5.00, False))
        order.add_item(DrinkItem("Coke", 2.00, "large"))
        
        bill = Bill(order)
        receipt = bill.generate()
        
        self.assertIn("Burger", receipt)
        self.assertIn("Coke", receipt)
        self.assertIn("£7.00", receipt)  # subtotal
        self.assertIn("£1.40", receipt)  # VAT
        self.assertIn("£8.40", receipt)  # total

    def test_factory_pattern(self):
        food = MenuItemFactory.create_item("food", "Pizza", 8.00, vegetarian=True)
        self.assertIsInstance(food, FoodItem)
        self.assertTrue(food.vegetarian)
        
        drink = MenuItemFactory.create_item("drink", "Tea", 1.50, size="small")
        self.assertIsInstance(drink, DrinkItem)
        self.assertEqual(drink.size, "small")

    def test_observer_pattern(self):
        class TestObserver(OrderObserver):
            def __init__(self):
                self.update_count = 0
            def update(self, order):
                self.update_count += 1
        
        order = Order()
        observer = TestObserver()
        order.add_observer(observer)
        
        order.add_item(FoodItem("Test", 1.00, False))
        order.add_item(FoodItem("Test2", 2.00, False))
        
        self.assertEqual(observer.update_count, 2)

    def test_empty_order_error(self):
        order = Order()
        bill = Bill(order)
        with self.assertRaises(ValueError):
            bill.generate()

    def test_invalid_item_name(self):
        with self.assertRaises(ValueError):
            FoodItem("", 5.00, False)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            FoodItem("Bad Item", -5.00, False)

    def test_customer(self):
        c = Customer("John Doe", "john@example.com")
        self.assertEqual(c.name, "John Doe")
        self.assertEqual(c.email, "john@example.com")
        
        c2 = Customer("Jane")
        self.assertEqual(c2.name, "Jane")
        self.assertIsNone(c2.email)
        
        with self.assertRaises(ValueError):
            Customer("")

    def test_order_customer_link(self):
        customer = Customer("Alice")
        order = Order(customer)
        self.assertEqual(order.customer, customer)
        
        bill = Bill(order)
        order.add_item(FoodItem("Cake", 3.00, True))
        receipt = bill.generate()
        self.assertIn("Customer: Alice", receipt)

if __name__ == '__main__':
    unittest.main()
