# 类的内部-对象属性操作

class Person:
    # 类的内部
    # 说明：类的内部，操作对象属性必须是在对象方法中
    def info(self):
        # TODO 设置属性
        # 语法：self.attr = value
        self.name = 'hello'
        # TODO 访问属性
        # 语法：self.attr
        # print(self.name)

    def get_info(self):
        # 访问属性
        print(self.name)

    def set_info(self):
        # TODO 修改属性
        # 语法：self.attr = new_value
        self.name = 'good'

    def del_info(self):
        # TODO 删除属性
        # 语法：del self.attr
        del self.name


# 类的外部
# 创建对象
p1 = Person()
p1.info()
print(p1.name)  # hello
p1.get_info() # hello

p1.set_info()
p1.get_info()  # good

# p1.del_info()
# p1.get_info()
