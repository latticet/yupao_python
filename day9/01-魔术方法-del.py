# 定义类
class Person:
    def __del__(self):
        print('del被执行了')


# 创建对象
p1 = Person()
# del p1

p2 = Person()
# del p2
