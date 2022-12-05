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
        """compares two products for identity"""
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __float__(self):

        return self.price
    
    def __repr__(self) -> str:
        return str(self.name)


class ShoppingCart:
    """class ShoppingCart implementation
    ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
    ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.
    """
    def __init__(self):
        products = []
        self.products = products
    
    def __len__(self):
        return len(self.products)

    def add_product(self, obj, quantity=1):
            self.products.append((obj, quantity))

    def total_price(self):
        sum = 0
        for product, quantity in self.products:
            sum = sum + product.get_total(quantity)
        return sum
   
    def __eq__(self, other: object) -> bool:
        """compares two products for identity"""
        if not isinstance(other, ShoppingCart):
            return False
        return True
   
    def __float__(self):
        return self.total_price()

    def __str__(self):
        return "".join(f"{product.__repr__()}: {quantity}, " for product, quantity in self.products)

    def __add__(self, other):
        if self.__eq__(other):
            self.products = self.products + other.products
            return self.products
        else:
            return print("You can add only cart to cart")         
        


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple = Product('apple', 10)
    juice = Product('juice', 30)
    cart = ShoppingCart()
    cart.add_product(apple, 1)
    cart.add_product(juice, 1)
    cart.add_product(apple, 1)
    print(cart.total_price())
    print(cart.__len__())
    apple2 = Product('apple', 0.5)
    print(apple.__eq__(apple2))
    print(apple.__float__(), apple.__str__())
    print(cart.__float__())
    cart2 = ShoppingCart()
    cart2.add_product(apple2, 2)
    print(cart.__float__())
    print(cart.__str__())
    cart2.__add__(cart)
    print(cart2.__str__())
    print(cart2.total_price())
    cart2.__add__(apple)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
