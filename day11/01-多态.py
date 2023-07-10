# 通过一个接口，传入不同的对象，调用相同的方法，产生不同的结果
# 多态实现：
"""
1. 有继承关系
2. 子类调用父类同名的方法
3. 通过一个接口（函数）统一调用
"""


# 动物类
class Animal:
    def call(self):
        print('动物叫')


# 猫类
class Cat(Animal):
    def call(self):
        # 开始时间
        print('喵喵喵')
        # 结束时间
        # 结束时间 - 开始时间


# 狗类
class Dog(Animal):
    def call(self):
        # 开始时间
        print('汪汪汪')
        # 结束时间
        # 结束时间 - 开始时间


# 人类
class Person(Animal):
    """
    def call(self):
        # 开始时间
        print('哈哈哈')
        # 结束时间
        # 结束时间 - 开始时间
    """
    pass


cat = Cat()
# cat.call()

dog = Dog()


# dog.call()


def do_call(obj):
    # 开始时间
    obj.call()
    # 结束时间
    # 结束时间 - 开始时间


# cat.call()
do_call(cat)
do_call(dog)
do_call(Person())
