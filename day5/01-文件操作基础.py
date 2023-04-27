# TODO 1. 打开文件
"""
文件资源句柄 = open(文件路径, 操作模式(读/写)='r:read', encoding='utf8')
"""
# f = open('resource/demo.txt', 'r', encoding='utf8')
f = open('resource/demo.txt', encoding='utf8')
# TODO 2. 操作文件
# 读
# 一次性读取文件中的所有内容
content = f.read()
print(content)
# 写

# TODO 3. 关闭文件
# f.close()
