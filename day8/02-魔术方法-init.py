# 定义人类
# __init__
# 触发：对象创建以后，init执行
# 作用：初始化对象属性

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建对象以后
p1 = Person('hello', 18)
print(p1.name)
print(p1.age)

p2 = Person('good', 19)
print(p2.name)
print(p2.age)
