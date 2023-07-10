# 单例模式是一种设计模式
# 单例模式：一个类只能创建一个对象

# 实现单例模式
class Singleton:
    instance = None  # 用来存创建出来的对象

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Singleton()
print(s1)

s2 = Singleton()
print(s2)

s3 = Singleton()
print(s3)
