# 私有权限
# 访问范围：类的属性和方法只能在类的内部访问
# 实现方式：
"""
__attr
__fn
"""


class Person:
    def __init__(self):
        self.name = 'hello'
        # 私有属性
        self.__age = 18
        # 受保护的属性
        self._xx = 100

    def set_age(self, age):
        if 0 < age < 121:
            self.__age = age
        else:
            print('输入年的不合法')

    def get_age(self):
        return self.__age


person = Person()
print(person._Person__age)
"""
print(person.get_age())

person.set_age(99)
print(person.get_age())
"""