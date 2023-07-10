# TODO __new__
"""
触发机制：创建对象时
作   用：用来创建对象, 返回结果
"""


class Demo(object):
    def __new__(cls, *args, **kwargs):
        pass


demo1 = Demo()
print(demo1)
