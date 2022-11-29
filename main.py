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
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_total(self, quantity):
        """calculating total price for product"""
        return round(quantity * self.price, 2)


class ShoppingCart:
    """class ShoppingCart implementation
    ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
    ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.
    """
    products_in_cart = []

    def add_product(self, obj, quantity):
        self.products_in_cart.append((obj, quantity))

    def total_price(self):
        sum = 0
        for product in self.products_in_cart:
            sum = sum + product[0].get_total(product[1])
        return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple = Product('apple', 10.43)
    print(apple.get_total(5))
    pear = Product('pear', 15)
    orange = Product('orange', 15)
    cart = ShoppingCart()
    cart.add_product(apple, 4.03)
    print(cart.products_in_cart)
    cart.add_product(pear, 3)
    cart.add_product(orange, 2)
    print(cart.total_price())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
