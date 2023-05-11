# TODO 1. 打开原文件，读取内容
f = open('resource/cat.webp', 'rb')
content = f.read()
f.close()

# TODO 2. 创建新文件，写入内容
f = open('resource/cat_副本.webp', 'wb')
f.write(content)
f.close()
