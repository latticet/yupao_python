# readlines：一次性读取所有行，返回列表。['line1', 'line2', ...]
f = open('resource/demo1.txt', encoding='utf8')
lines = f.readlines()
f.close()

print(lines)
