class Product:
    product_count = 0

    def __init__(self, name, category, price, quantity):
        self.id = Product.product_count + 1
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        Product.product_count += 1

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Category: {self.category}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_stock(self, product_id, new_quantity):
        for product in self.products:
            if product.id == product_id:
                product.quantity = new_quantity

    def retrieve_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def stock_report(self):
        return '\n'.join([str(product) for product in self.products])

    def sales_history(self, transactions):
        return '\n\n'.join([str(transaction) for transaction in transactions])

    def revenue_report(self, transactions):
        return sum([transaction.total_amount for transaction in transactions])
    
class Transaction:
    def __init__(self):
        self.items = []
        self.total_amount = 0

    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append((product, quantity))
            self.total_amount += product.price * quantity
            product.quantity -= quantity
        else:
            print(f"Only {product.quantity} of {product.name} available.")

    def __str__(self):
        return '\n'.join([f"{item[0].name} ({item[1]}) - ${item[0].price * item[1]}" for item in self.items]) + f"\nTotal Amount: ${self.total_amount}"

