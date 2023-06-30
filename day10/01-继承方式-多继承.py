# 语法：
"""
class A(B, C, D):
    pass
"""


# 定义2个父类
# Person
class Person:
    def talk(self):
        print('说话')


# Pig
class Pig:
    def eat(self):
        print('吃东西')


# PeiQ
# 继承Person，Pig
class PeiQ(Person, Pig):
    pass


# 创建PeiQ对象
pei_q = PeiQ()
pei_q.talk()
pei_q.eat()
