# I am creating the class  phone
class Iphone:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def reduce_price(self, amount):
        self.price = self.price - amount
        return self.price

charles = Iphone ("Samsung", "A17", 25000)


print("Model:", charles.model)
print("Brand:", charles.brand)
print("Original price:", charles.price)
print("New price:", charles.reduce_price(5000))