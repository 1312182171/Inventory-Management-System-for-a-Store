Inventory Management System (IMS)

Introduction
The IMS is designed to help stores in organizing their products, comparing stock levels, recording sales, and generating reports. Using Python, this program gives the user an efficient way of managing their inventories/

Implemented Functionalities:

Product Creation and Tracking:

Products are identified with attributes like ID, name, category, price, and quantity.
Each product is an instance of the Product class.


Inventory Management:

Products are added to the inventory.
Stock levels of products in the inventory can be updated and changed based on demands.
Specific product information can be retrieved from the inventory.
All these functionalities are provided by the Inventory class.


Sales and Transactions:

Sales transactions are recorded, indicating the products sold, their quantities, and the total transaction amount.
Every transaction is an instance of the Transaction class.


Reporting:

Current stock levels can be generated.
Sales history report provides details of all transactions.
Revenue report calculates the total revenue from all transactions.

Test Results:


Adding Products to Inventory
Input:
p1 = Product("Laptop", "Electronics", 1000, 10)
p2 = Product("Mobile Phone", "Electronics", 500, 50)
p3 = Product("Shirt", "Apparel", 20, 100)
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

Output:
ID: 1, Name: Laptop, Category: Electronics, Price: $1000, Quantity: 10
ID: 2, Name: Mobile Phone, Category: Electronics, Price: $500, Quantity: 50
ID: 3, Name: Shirt, Category: Apparel, Price: $20, Quantity: 100

Recording Transaction:
Input: 
transaction1 = Transaction()
transaction1.add_product(p1, 2)
transaction1.add_product(p3, 5)

Output:
Laptop (2) - $2000
Shirt (5) - $100
Total Amount: $2100

Updated Inventory:
ID: 1, Name: Laptop, Category: Electronics, Price: $1000, Quantity: 8
ID: 2, Name: Mobile Phone, Category: Electronics, Price: $500, Quantity: 50
ID: 3, Name: Shirt, Category: Apparel, Price: $20, Quantity: 95

Report:
Input:
transaction2 = Transaction()
transaction2.add_product(p2, 3)
transaction2.add_product(p3, 10)

Output:
Sales History:
Laptop (2) - $2000
Shirt (5) - $100
Total Amount: $2100

Mobile Phone (3) - $1500
Shirt (10) - $200
Total Amount: $1700

Total Revenue: $3800


I think that the result of this program is fairly okay. There are some potential improves like the UI design and the error handling.






