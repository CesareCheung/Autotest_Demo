#! usr/bin/env python
# coding=utf-8
# Author="张维序"

import os

# print(os.system("ipconfig"))

# 获取当前文件目录
# print(dir(os))
# 创建目录
# os.mkdir("E:\Autotest_Demo\log")
# 删除目录
# os.rmdir("E:\Autotest_Demo\log")
# 对文件或目录重命名
os.rename("E:\Autotest_Demo\log", "E:\Autotest_Demo\log")
# 当前文件所在目录
print(os.path.dirname(__file__))
# 文件当前目录的上级目录
print(os.path.dirname(os.path.dirname(__file__)))

# 实现对E:\Autotest_Demo下login.md文件内容读取
base_dir = os.path.dirname(os.path.dirname(__file__))
f = open(os.path.join(base_dir, "Autotest_Demo/login.md"), 'r')
print(f.read())
