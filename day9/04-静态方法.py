# 定义类
class Person:
    @staticmethod
    def get_info():
        print('hello python')

    def get_name(self):
        print('name')

    @classmethod
    def get_country(cls):
        print('country')


# 静态方法
"""
1. 定义在类中的函数
2. 需要添加一个装饰器
"""

# 静态方法调用
# 1. 通过类名调用（推荐）
Person.get_info()

# 2. 通过对象调用
p1 = Person()
p1.get_info()

# 小结
"""
1. 对象方法
2. 类方法
3. 静态方法
"""
# 三种方法使用选择
"""
如果一个方法中需要用到对象属性，那么就定义为对象方法。
如果一个方法中需要用到类属性，那么就定义为类方法。
如果一个方法中既没有用到对象属性，也没有用到类属性，那么就可以定位静态方法。
如果你选择不了用这3种中的哪个方法，那么直接选择用对象方法。
"""
