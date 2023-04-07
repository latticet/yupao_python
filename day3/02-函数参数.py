# 需求1： 1 + 2的函数
# 定义
def add1():
    result = 1 + 2
    print(result)


# 调用
add1()


# 需求2： 2 + 2的函数
def add2():
    result = 2 + 2
    print(result)


# 需求2： 3 + 2的函数
def add3():
    result = 3 + 2
    print(result)


# 参数
"""
语法：
def fn(参数1, 参数2， 参数n):
    函数体
"""

print('==' * 20)


# 定义
def add(a, b):    # 把函数定义时的参数叫做形式参数：形参
    result = a + b
    print(result)


# 调用
add(1, 2)   # 把函数调用时的参数叫做实际参数：实参
add(2, 3)
add(5, 10)
