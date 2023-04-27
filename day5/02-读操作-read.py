# 1. 打开文件
# f = open('resource/demo.txt', 'r', encoding='utf8')
# 注意：如果模式是二级制模式的时候，不能写第三个参数
f = open('resource/demo.txt', 'rb')

# 2. 操作文件
# TODO 文本模式的读 r
# 作用：读取普通文本
# size:文本的字符个数
"""
while True:
    content = f.read(5)
    if not content:
        break
    print(content)
"""

# TODO 二进制模式的读b:bytes
# 作用：用在读取图片，视频。
# size:字节大小  3个字节1个汉字 1kb = 1024Bytes  1MB = 1024kb 1GB = 1024M 1T 1024GB
while True:
    content = f.read(2)
    if not content:
        break
    # 二进制转字符串
    print(content.decode())

# 3. 关闭文件
f.close()
