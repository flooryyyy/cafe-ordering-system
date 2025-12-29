# UML Class Diagram

[UML Class Diagram for the Cafe Ordering System](diagrams/ap-class-diagram-light.png)

The cafe ordering system was designed with scalability and modularity in mind to ensure optimal implementations of menu management, order processing, and bill generation by using object-oriented principles. UML diagrams were used to visualise the system’s architecture and interactions before proceeding with the implementation. 

Figure 1 showcases the core classes and their relationships. An abstract MenuItem class defines the foundational fields and methods which FoodItem and DrinkItem can inherit to prevent duplication. This also allows new item types to be added with ease in the future, while allowing specialised attributes to be assigned. 

Order class uses composition to hold one or more OrderLine objects. Each OrderLine represents a line on the receipt and contains a menu item and its quantity. This approach simplifies price calculations and allows future feature implementations such as item or clearance discounts. 

The Factory pattern is implemented through MenuItemFactory to centralise the creation of menu items. This improves the maintainability and scalability of code by allowing new menu item types to be implemented without modifying existing code. 

Lastly, the Observer pattern is implemented by allowing Order class to notify OrderObserver when an order is updated. This separates order implementation from order observer components, modularising the system and supporting future implementations like live status updates.

# Use Case Diagram
[Use Case Diagram showing Staff interactions](diagrams/ap-use-case-diagram-light.png)

The ordering system will be used by the cafe’s staff members. Figure 2 showcases the different possible use cases, covering management of menu items, creation of orders, and billing customers. The diagram helps define the functional requirements and scope of the system from the staff’s perspective. 

# Sequence Diagram
[Sequence Diagram showing the sequential steps of adding an item to order](diagrams/ap-sequence-diagram-light.png)

Figure 3 showcases the sequence of interactions for adding items to an order. The sequence begins with a staff member selecting an item and adding it to the order, resulting in the creation of an OrderLine to show the item with its quantity and sending an update to the order observer. 