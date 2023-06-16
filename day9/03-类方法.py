# 定义类
class Person:
    country = '中国'

    # TODO 定义类方法
    @classmethod
    def get_county(cls):
        print(cls.country)
        # print(cls)

    @classmethod
    def set_country(cls):
        cls.country = 'China'


# TODO 调用类方法
# 语法：类名.类方法名()
Person.get_county()
print(Person)

Person.get_county()
Person.set_country()
Person.get_county()



# 类方法定义
"""
1. 在类的内部定义
2. 必须要写一个cls的参数
3. 必须要写一个装饰器(语法形式)
4. 其他的和函数相同
"""
# cls
"""
cls指向当前类
"""

# 类方法应用
"""
类方法一般配合类属性使用
"""
