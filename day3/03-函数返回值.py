# 需求1：求任意2个数的和
def add1(a, b):
    print(a + b)


"""
add1(1, 2)
add1(3, 2)
add1(5, 2)
"""

# 函数返回值
# 返回函数的运行结果
"""
语法：
return 要返回的数据
说明：
返回到函数调用的地方
return 执行后会结束函数运行。
"""


def add2(a, b):
    result = a + b
    return result


x = add2(1, 2)
print(x)
