class Product:
    name: str
    description: str
    price: float
    quantity: int
    colour: int

    def __init__(self, name, description, price, quantity, colour):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.colour = colour


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


class Smartphone(Product):
    power: int
    model: str
    volume: float

    def __init__(self, name, description, price, quantity, colour, power, model, volume):
        super().__init__(name, description, price, quantity, colour)
        self.power = power
        self.model = model
        self.volume = volume

    def __add__(self, other):
        if type(self) == type(other):
            result = (self.price * self.quantity) + (other.price * other.quantity)
            return result
        else:
            raise TypeError


class Grass(Product):
    country: str
    time: float

    def __init__(self, name, description, price, quantity, colour, country, time):
        super().__init__(name, description, price, quantity, colour)
        self.counrty = country
        self.time = time

    def __add__(self, other):
        if type(self) == type(other):
            result = f'{self.country}, {other.country}'
            return result
        else:
            raise TypeError

iphone = Smartphone('telefon', 'good', 990,10,'green',123, '13iph',128)
iphone2 = Smartphone('tele2fon', 'go2od', 9920,102,'gr2een',1232, '132iph',1228)
print(iphone + iphone2)