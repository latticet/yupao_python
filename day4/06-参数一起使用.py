"""
print('hello', 'world', 'good', 'xx', 'xx', 'xx', 'xx', sep='-', end='|')
print('xx')
print('xx')
"""


# 所有参数使用：必填参数->位置不定长->默认参数->关键字不定长

def fn(a, *args, b=2, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)


fn(1, 'aa', 'bb', 'cc')
print('--' * 20)
fn(1, 'aa', 'bb', 'cc', x=100)
print('--' * 20)
fn(1, 'aa', 'bb', 'cc', x=100, b=200)
