def info(name, age, class_name='yupao'):
    print(f'name:{name}, age:{age}, class_name:{class_name}')


# 默认参数
# 给形参设置一个默认值

info('hello1', 18, 'xx')
info('hello2', 19)
info('hello3', 10)
info('hello4', 100)
info('hello4', 100, 'okk')

# 关键字传参
info( age=19, name='good', class_name='okk')
