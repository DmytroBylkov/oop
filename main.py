# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
Challenge:
#. Implement ``Product`` class
#. Each ``Product`` instance should implement properties:
    * ``name`` - a product's name, like apple, cheese etc.
    * ``price`` - a price for a single unit
#. ``Product`` instance should have a behavior of calculating total
   price for a specified quantity of goods
#. Implement ``ShoppingCart`` class
#. ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
#. ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.
"""


class Product:
    """class Product imlementation
    * ``name`` - a product's name, like apple, cheese etc.
    * ``price`` - a price for a single unit
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_total(self, quantity: float):
        """calculating total price for product"""
        return round(quantity * self.price, 2)

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class ShoppingCart:
    """class ShoppingCart implementation
    ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
    ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.
    """
    def __init__(self):
        products_in_cart = []
        self.products_in_cart = products_in_cart
    
    def __len__(self):
        return len(self.products_in_cart)

    def add_product(self, obj, quantity):
        self.products_in_cart.append((obj, quantity))

    def total_price(self):
        sum = 0
        for product, quantity in self.products_in_cart:
            sum = sum + product.get_total(quantity)
        return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple = Product('apple', 10.59)
    juice = Product('juice', 36.55)
    cart = ShoppingCart()
    cart.add_product(apple, 0.35)
    cart.add_product(juice, 4)
    cart.add_product(apple, 0.35)
    print(cart.total_price())
    print(cart.__len__())
    apple2 = Product('apple', 10.59)
    print(apple.__eq__(apple2))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
