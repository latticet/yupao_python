# 三个数求和
def add1(a, b, c):
    return a + b + c


# TODO 位置不定长
"""
语法：
def fn(*args):
    args: 将所有的位置方式传入的实参收集在这个元组中
"""


# 任意多个数求和
def add2(*args):
    # print(args)  # 元组  (10, 20, 30)
    count = 0
    for i in args:
        count += i
    return count


# 位置传参
# print(add2(1, 2, 3, 1, 1))

# TODO 关键字不定长
"""
语法：
def fn(**kwargs):  kw:keyword args:arguments
    kwargs:收集以关键字传入的实参，存储在字典
"""


def add3(**kwargs):
    print(kwargs)  # dict {'a':1, 'b':2}


add3(a=1, b=2, x=100, y=200)


