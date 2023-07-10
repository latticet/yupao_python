# TODO type 查看数据(对象)类型
print(type('hello'))
print(type(111))
print(type([1, 2]))

class Demo:
    pass

demo1 = Demo()
print(type(demo1))

# TODO dir
print(dir('hello'))


# TODO isinstance 查看对象是否属于某个类. True|False
print(isinstance(demo1, Demo))
print(isinstance('hello', Demo))