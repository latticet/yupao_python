# 商品类
class Goods:
    def __init__(self):
        self.name = '商品'
        self.price = 100


# 手机类
class Phone(Goods):
    def __init__(self):
        self.name = 'iphone14'
        self.price = 200

phone = Phone()
print(phone.name)
print(phone.price)

