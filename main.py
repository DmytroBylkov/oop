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


    def calculating_total_price_for_product(self, quantity_of_goods):
        return quantity_of_goods * self.price


class ShoppingCart:
    """class ShoppingCart implementation
    ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
    ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.
    """
    products_in_cart = []


    def add_product(self, obj, amount):
        self.products_in_cart.append((obj.name,obj.price, amount))


    def total_price(self):
        sum = 0
        for product in self.products_in_cart:
            sum = sum + product[1] * product[2]
        return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple = Product('apple', 10)
    print(apple.calculating_total_price_for_product(5))
    pear = Product('pear', 15)
    orange = Product('orange', 15)
    cart = ShoppingCart()
    cart.add_product(apple, 2)
    print(cart.products_in_cart)
    cart.add_product(pear, 1)
    cart.add_product(orange, 4)
    print(cart.total_price())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
