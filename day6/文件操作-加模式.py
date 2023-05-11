# +:扩展模式。不能单独使用。必须配合rwa来使用。
# r+: 读写
# w+: 读写
# a+: 读写

# 打开文件
f = open('resource/demo3.txt', 'w+', encoding='utf8')
# 操作文件
f.write('hello python')
# 移动光标
f.seek(0)
content = f.read()  # 读不出来
print(content)
# 关闭文件
f.close()

# r
# w
# a
# b
# +
