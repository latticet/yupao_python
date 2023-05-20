# 对象方法
# 定义类
class Person:
    # 方法定义
    def eat(self):
        # 方法体
        print('self:', self)
        print('吃火锅')


# 创建对象
p1 = Person()
print('p1:', p1)

# 方法使用
# 语法：对象.方法名()  obj.fn()
p1.eat()

# 创建对象
p2 = Person()
print('p2:', p2)
p2.eat()


# 对象方法说明:
"""
1. 在类的内部定义
2. 定义方式和函数有一点不同，必须传入一个叫做self的参数
3. 使用方式和函数基本相同
4. python解释器会把当前调用这个方法的对象传给self
"""

# self
"""
self:当前对象。谁调用当前这个方法，self就是谁。
"""
