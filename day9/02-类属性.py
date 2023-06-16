# 定义类
class Person:
    # TODO 类的内部定义
    country = '中国'


# TODO 类的外部定义
# 语法：类名.类属性名 = 属性值
Person.code = '001'

# TODO 类属性的访问
# 语法：类名.属性名
print(Person.code)
print(Person.country)

# TODO 类型属性修改
# 语法：类型.属性名 = 属性值
Person.country = 'China'

print(Person.country)
