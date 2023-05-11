# TODO 打开文件
# open(路径, 模式, 编码方式)
# w:write 覆盖写。如果文件不存在会创建，如果存在有内容会被覆盖
f = open('resource/demo1.txt', 'w', encoding='utf8')
# TODO 操作文件
# write：一次性写入内容
"""
f.write('123')
"""
# writelines：一次写入多个内容
f.writelines(['def', '456', 'abc'])
# TODO 关闭文件
f.close()
