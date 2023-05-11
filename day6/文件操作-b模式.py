# TODO b:bytes 二进制。不能单独使用，必须配合rwa来使用
# 打开文件
# rb: 二进制方式的读
# r: 文本方式的读
# 注意：如果是二进制模式，就不能写encoding了。
f = open('resource/cat.webp', 'rb')
# 操作文件
content = f.read()
print(content)
# 关闭文件
f.close()
