# Inventory_Mang_Sys_PY
🏬 Inventory and Order Management System
This Python project is a basic Inventory and Order Management System designed to simulate real-world warehouse, supplier, and product operations using object-oriented programming (OOP) principles. It features polymorphism, abstraction, encapsulation, and inheritance, making it a great educational tool for understanding core OOP concepts in Python.

📦 Features
Product Hierarchy
Abstract base class Product is extended by specialized classes:

Electronic (with warranty)

Furniture (with material type)

Encapsulated Inventory Handling
Stock quantities and supplier details are managed using getter/setter methods.

Supplier Management
Each product is linked to a Supplier instance, which holds details such as name and contact.

Order Placement
Orders can be placed only if sufficient stock is available. A simple validation mechanism updates inventory accordingly.

Warehouse Abstraction
An abstract base class Warehouse is extended by LocalWarehouse and CentralWarehouse, simulating different inventory locations using polymorphism.

Time-stamped Orders
Orders include an auto-generated date using the datetime module.

🛠 Technologies Used
Python 3.x

OOP Concepts: Abstraction, Inheritance, Encapsulation, Polymorphism

abc module for abstract base classes

datetime module for order time stamping

📋 Example Output

Product Details:
Product ID: 101, Name: Laptop, Price: 50000, Stock: 10
Warranty Period: 24 months

Product ID: 201, Name: Office Chair, Price: 3500, Stock: 5
Material: Leather

Order placed for 1 unit(s) of Laptop.
Order placed for 3 unit(s) of Office Chair.
Insufficient stock for Office Chair.

Order Details:
Order ID: 1, Product: Laptop, Quantity: 1, Date: 2025-07-20
Order ID: 2, Product: Office Chair, Quantity: 3, Date: 2025-07-20

Laptop Stock: 9
Chair Stock: 2

Supplier Info:
Supplier ID: 1, Name: ABC Electronics, Contact: 9876XXXXXX
Supplier ID: 2, Name: Furniture House, Contact: 9123XXXXXX

Warehouse Tracking:
Tracking inventory in Local Warehouse...
Tracking inventory in Central Warehouse...

📚 Learning Goals
This project demonstrates:

Effective use of class-based architecture

How to use abstraction for code flexibility

Realistic simulation of a basic supply chain system

How to model relationships between products, suppliers, and orders

