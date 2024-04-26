from abc import ABC, abstractmethod

class MixinRepr:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}, {self.__dict__}'

class Base_Product(ABC):
    @abstractmethod
    def new_product(self):
        pass

class Product(Base_Product, MixinRepr):
    name: str
    description: str
    price: float
    quantity: int
    colour: str

    def __init__(self, name, description, price, quantity, colour):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.colour = colour


    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        for product in products:
            if name == product.name:
                quantity += product.quantity
                if price < price(product):
                    price = price(product)
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
        if type(self) == type(other):
            result = (self.price * self.quantity) + (other.price * other.quantity)
            return result
        else:
            raise TypeError



class Smartphone(Product, MixinRepr):
    power: int
    model: str
    volume: float

    def __init__(self, name, description, price, quantity, colour, power, model, volume):
        super().__init__(name, description, price, quantity, colour)
        self.power = power
        self.model = model
        self.volume = volume


class Grass(Product, MixinRepr):
    country: str
    time: float

    def __init__(self, name, description, price, quantity, colour, country, time):
        super().__init__(name, description, price, quantity, colour)
        self.counrty = country
        self.time = time


iphone = Smartphone('telefon', 'good', 990,10,'green',123, '13iph',128)
iphone2 = Smartphone('tele2fon', 'go2od', 9920,102,'gr2een',1232, '132iph',1228)
print(iphone + iphone2)