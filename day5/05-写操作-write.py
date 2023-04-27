# 打开文件
# mode:
# w: 覆盖写，如果文件不存在会创建文件。如果文件存在，会覆盖原有内容写入新内容。
# f = open('resource/demo3.txt', 'w', encoding='utf8')
f = open('resource/demo.txt', 'w', encoding='utf8')

# 操作文件
# 语法：f.write(content)
f.write('今天天气不错，适合好好上班')

# 关闭文件
f.close()
