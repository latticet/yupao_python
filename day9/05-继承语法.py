# 继承语法
# B类继承了A类
# A：父类
# B: 子类
"""
class A:
    pass

class B(A):
    pass
"""


class A:
    def __init__(self):
        self.name = 'hello'
        self.age = 18


class B(A):
    pass


b = B()
print(b.name)
print(b.age)
