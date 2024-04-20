class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        for product in products:
            if name == product.name:
                quantity += product.quantity
                if price < product.__price:
                    price = product.__price
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Введена некорректная цена.")
        else:
            self.__price = new_price

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        result = (self.price * self.quantity) + (other.price * other.quantity)
        return result