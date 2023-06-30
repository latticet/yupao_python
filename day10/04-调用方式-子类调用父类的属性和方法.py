# 商品类
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print('goods_info')


# 手机类
class Phone(Goods):
    def __init__(self, name, price, capacity):
        # super()：指向当前的父类
        super().__init__(name, price)
        self.capacity = capacity

    def info(self):
        super().info()  # 调用父类的info方法
        print('phone_info')


phone = Phone('iphone14', 1000, 128)
print(phone.name)
print(phone.price)
print(phone.capacity)
phone.info()


# 衣服类
class Coat(Goods):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
