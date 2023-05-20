# 类的外部-对象属性

# 定义类
class Person:
    # 类的内部
    pass


# 创建对象
p1 = Person()

# 类的外部
# TODO 设置属性
# 语法：对象.属性名 = 属性值   obj.attr = value
p1.name = 'hello'
p1.age = 18

# TODO 查看属性
# 语法：obj.attr
print(p1.name)
print(p1.age)

# TODO 修改属性
# 语法：obj.attr = value
p1.name = 'good'
print(p1.name)

# TODO 删除属性
# del obj.attr
del p1.name
print(p1.name)
