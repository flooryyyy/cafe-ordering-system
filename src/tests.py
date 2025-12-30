import unittest

from menu import Menu, FoodItem, DrinkItem
from order import Order
from bill import Bill
from factory import MenuItemFactory
from observer import OrderObserver
from customer import Customer
from rich.panel import Panel

class TestCafeSystem(unittest.TestCase):  
    def test_food_item(self):
        # make sure food items store data correctly
        burger = FoodItem("Burger", 5.00, False)
        self.assertEqual(burger.name, "Burger")
        self.assertEqual(burger.price, 5.00)
        self.assertEqual(burger.vegetarian, False)
        
    def test_order_calculations(self):
        order = Order()
        burger = FoodItem("Burger", 5.00, False)
        coke = DrinkItem("Coke", 2.00, "large")
        
        # add some stuff to the order
        order.add_item(burger)
        order.add_item(coke)
        
        # check if the math is mathing
        self.assertEqual(order.get_total(), 7.00)
        self.assertAlmostEqual(order.get_vat(), 1.40) # 20% of 7
        self.assertAlmostEqual(order.get_total_cost(), 8.40)

    def test_menu_management(self):
        menu = Menu()
        item = FoodItem("Test", 1.00, True)
        
        # try adding and removing
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
        
        # bill.generate() returns a rich Panel now, so just check it's the right type
        self.assertIsInstance(receipt, Panel)
        
        # double check the order total is still correct inside the bill
        self.assertEqual(bill.order.get_total_cost(), 8.40)

    def test_factory_pattern(self):
        # testing if the factory actually makes the right stuff
        food = MenuItemFactory.create_item("food", "Pizza", 8.00, vegetarian=True)
        self.assertIsInstance(food, FoodItem)
        self.assertTrue(food.vegetarian)
        
        drink = MenuItemFactory.create_item("drink", "Tea", 1.50, size="small")
        self.assertIsInstance(drink, DrinkItem)
        self.assertEqual(drink.size, "small")

    def test_observer_pattern(self):
        # simple observer to count updates
        class TestObserver(OrderObserver):
            def __init__(self):
                self.update_count = 0
            def update(self, order):
                self.update_count += 1
        
        order = Order()
        observer = TestObserver()
        order.add_observer(observer)
        
        # should trigger update twice
        order.add_item(FoodItem("Test", 1.00, False))
        order.add_item(FoodItem("Test2", 2.00, False))
        
        self.assertEqual(observer.update_count, 2)

    def test_empty_order_error(self):
        # can't print a bill for nothing
        order = Order()
        bill = Bill(order)
        with self.assertRaises(ValueError):
            bill.generate()

    def test_invalid_item_name(self):
        # should crash if name is empty
        with self.assertRaises(ValueError):
            FoodItem("", 5.00, False)

    def test_negative_price(self):
        # prices can't be negative
        with self.assertRaises(ValueError):
            FoodItem("Bad Item", -5.00, False)

    def test_customer(self):
        c = Customer("John Doe", "john@example.com")
        self.assertEqual(c.name, "John Doe")
        
        # checking optional email
        c2 = Customer("Jane")
        self.assertEqual(c2.name, "Jane")
        self.assertIsNone(c2.email)
        
        # name is required
        with self.assertRaises(ValueError):
            Customer("")

    def test_order_customer_link(self):
        # linking a customer to an order
        customer = Customer("Alice")
        order = Order(customer)
        self.assertEqual(order.customer, customer)
        
        bill = Bill(order)
        order.add_item(FoodItem("Cake", 3.00, True))
        
        # just checking if the code runs for now
        receipt = bill.generate()
        self.assertIsInstance(receipt, Panel)

if __name__ == '__main__':
    unittest.main()
