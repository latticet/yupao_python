import os
import shutil

# TODO os.rename("文件路径","新文件名")  修改文件名
# demo1.txt my_demo1.txt
# os.rename('resource/demo1.txt', 'resource/my_demo1.txt')

# TODO os.remove(文件路径)  # 删除文件
# os.remove('resource/my_demo1.txt')

# TODO os.mkdir ("文件夹路径")  创建目录
# os.mkdir('resource/dir1')

# TODO os.getcwd() # 获取当前脚本所在的路径
# print(os.getcwd())

# TODO os.chdir()  # 切换目录
# cd：切换目录
# print(os.getcwd())
# os.chdir('resource')
# print(os.getcwd())

# TODO os.listdir("目录路径") # 列出目录下的资源
# ls: linux
# dir: window
# print(os.listdir('resource'))

# TODO os.rmdir("目录路径") 删除空目录
# os.rmdir('resource/dir2')  # 能删除，因为是空的
# os.rmdir('resource/dir1')  # 不能删除，因为里面有内容

# TODO shutil.rmtree('目录路径') # 删除目录（包括非空目录）
# shutil.rmtree('resource/dir1')

# TODO os.path.isdir() # 判断资源是目录
# TODO os,path.isfile() # 判断资源是文件
"""
print(os.path.isdir('resource'))  # True
print(os.path.isdir('小练习-图片复制.py'))  # False

print(os.path.isfile('resource'))  # False
print(os.path.isfile('小练习-图片复制.py'))  # True
"""

# TODO os.path.splitext ("文件名")  # 获取一个完整文件名的，文件名和扩展名
# demo1.txt   demo1 .txt
# ('demo1', '.txt')
print(os.path.splitext('小练习-图片复制.py'))  # ext:extension  (小练习-图片复制, '.py')
