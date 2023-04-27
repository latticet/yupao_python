# readline:每次读取一行
# 打开文件
f = open('resource/demo1.txt', 'r', encoding='utf8')
# 操作文件
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
# 关闭文件
f.close()
