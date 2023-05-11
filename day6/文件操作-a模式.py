# TODO a:append 追加写。如果文件不存在，会创建。
# f = open('resource/demo1.txt', 'a', encoding='utf8')
f = open('resource/demo2.txt', 'a', encoding='utf8')
# 写入内容
f.write('hello')
# 关闭文件
f.close()