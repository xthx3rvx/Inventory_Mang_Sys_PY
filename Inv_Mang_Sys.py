from abc import ABC, abstractmethod
from datetime import datetime

class Warehouse(ABC):
    @abstractmethod
    def trackInventory(self):
        pass

class LocalWarehouse(Warehouse):
    def trackInventory(self):
        print("Tracking inventory in Local Warehouse...")

class CentralWarehouse(Warehouse):
    def trackInventory(self):
        print("Tracking inventory in Central Warehouse...")

class Supplier:
    def __init__(self, supplierID, name, contact):
        self.supplierID = supplierID
        self.name = name
        self.contact = contact

    def displaySupplier(self):
        print(f"Supplier ID: {self.supplierID}, Name: {self.name}, Contact: {self.contact}")

class Product:
    def __init__(self, productID, name, price, stockQuantity, supplierInfo):
        self.productID = productID
        self.name = name
        self.price = price
        self.__stockQuantity = stockQuantity     
        self.__supplierInfo = supplierInfo        

    def getStockQuantity(self):
        return self.__stockQuantity

    def setStockQuantity(self, qty):
        self.__stockQuantity = qty

    def getSupplierInfo(self):
        return self.__supplierInfo

    def setSupplierInfo(self, supplier):
        self.__supplierInfo = supplier

    def getDetails(self):
        print(f"Product ID: {self.productID}, Name: {self.name}, Price: {self.price}, Stock: {self.__stockQuantity}")

class Electronic(Product):
    def __init__(self, productID, name, price, stockQuantity, supplierInfo, warrantyPeriod):
        super().__init__(productID, name, price, stockQuantity, supplierInfo)
        self.warrantyPeriod = warrantyPeriod

    def getDetails(self): 
        super().getDetails()
        print(f"Warranty Period: {self.warrantyPeriod} months")

class Furniture(Product):
    def __init__(self, productID, name, price, stockQuantity, supplierInfo, material):
        super().__init__(productID, name, price, stockQuantity, supplierInfo)
        self.material = material

    def getDetails(self):  
        super().getDetails()
        print(f"Material: {self.material}")

class Order:
    def __init__(self, orderID, product, quantity, orderDate):
        self.orderID = orderID
        self.product = product
        self.quantity = quantity
        self.orderDate = orderDate

    def displayOrder(self):
        print(f"Order ID: {self.orderID}, Product: {self.product.name}, Quantity: {self.quantity}, Date: {self.orderDate.date()}")

def placeOrder(product, quantity=1):
    if product.getStockQuantity() >= quantity:
        product.setStockQuantity(product.getStockQuantity() - quantity)
        print(f"Order placed for {quantity} unit(s) of {product.name}.")
    else:
        print(f"Insufficient stock for {product.name}.")

if __name__ == "__main__":
    supplier1 = Supplier(1, "ABC Electronics", "9876XXXXXX")
    supplier2 = Supplier(2, "Furniture House", "9123XXXXXX")

    laptop = Electronic(101, "Laptop", 50000, 10, supplier1, 24)
    chair = Furniture(201, "Office Chair", 3500, 5, supplier2, "Leather")

    print("Product Details:")
    laptop.getDetails()
    print()
    chair.getDetails()
    print()

    placeOrder(laptop)
    placeOrder(chair, 3)
    placeOrder(chair, 10)  
    print()

    order1 = Order(1, laptop, 1, datetime.now())
    order2 = Order(2, chair, 3, datetime.now())
    print("Order Details:")
    order1.displayOrder()
    order2.displayOrder()
    print()

    print(f"Laptop Stock: {laptop.getStockQuantity()}")
    print(f"Chair Stock: {chair.getStockQuantity()}")
    print()

    print("Supplier Info:")
    laptop.getSupplierInfo().displaySupplier()
    chair.getSupplierInfo().displaySupplier()
    print()

    print("Warehouse Tracking:")
    lw = LocalWarehouse()
    cw = CentralWarehouse()
    lw.trackInventory()
    cw.trackInventory()
