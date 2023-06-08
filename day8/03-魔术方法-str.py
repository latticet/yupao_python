# 定义人类
# __str__
# 触发：对象被print打印的时候
# 作用：返回对象的关键数据
# 注意：str魔术方法必须返回字符串

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # print('str被执行了')
        return self.name + ':' + str(self.age)

    def __del__(self):  # 析构函数
        print('del被执行')


# 创建对象
p1 = Person('hello', 18)
print(p1)

p2 = Person('good', 19)
print(p2)
