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
        return 'Product'
      
    def __str__(self) -> str:
        return f'{self.name}'        


class ShoppingCart:
    """class ShoppingCart implementation
    ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
    ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.
    """
    def __init__(self):
        self.products = []
    
    def __len__(self):
        return len(self.products)
   
    def __repr__(self) -> str:
        return 'ShoppingCart'   
   
    def __add__(self, other, quantity=1):
        if other.__repr__() == 'Product':
            self.products.append((other, quantity))
            return self.products
        elif other.__repr__() == 'ShoppingCart':
            self.products = self.products + other.products
            return self.products
        else:
            print("You can add only cart to cart, or product to cart")
            return self.products
   
    def total_price(self):
        sum = 0
        for product, quantity in self.products:
            sum = sum + product.get_total(quantity)
        return sum
   
    def __eq__(self, other: object) -> bool:
        """compares two products for identity"""
        if not isinstance(other, ShoppingCart):
            return False
        return self.__str__() == other.__str__()
   
    def __float__(self):
        return self.total_price()

    def __str__(self):
        return ", ".join(f"{product.__repr__()}: {quantity}" for product, quantity in self.products)

           


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple = Product('apple', 10)
    juice = Product('juice', 30)
    cart = ShoppingCart()
    cart.add_product(apple, 1)
    cart.add_product(juice, 1)
    cart.add_product(apple, 1)
    apple2 = Product('apple', 0.5)
    cart2 = ShoppingCart()
    cart2.add_product(apple2, 2)
    print(apple.__repr__())
    print(cart.__str__())
    print(cart2.__str__())
    cart.__add__(cart2)
    print(cart.__str__())
    cart.__add__(juice, 3)
    print(cart.__str__())
    print(cart.total_price())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
