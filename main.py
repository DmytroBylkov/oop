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


    def __init__(self, name: str, price: int, amount: int):
        self.name = name
        self.price = price
        self.amount = amount

    def total_price(self):
        return self.amount * self.price


class ShoppingCart:
    product_in_basket = {}

    def add_product(self,obj):
        self.product_in_basket.update([(obj.name, obj.total_price())])

    @property
    def totalCostOfProducts(self):
        sum = 0
        for product in self.product_in_basket:
            sum = sum + self.product_in_basket[product]
        return sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    apple = Product('apple', 10, 5)

    pear = Product('pear', 15, 3)

    orange = Product('orange', 15, 2)

    basket = ShoppingCart()
    basket.add_product(apple)
    basket.add_product(pear)
    basket.add_product(orange)
    print(basket.totalCostOfProducts)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
