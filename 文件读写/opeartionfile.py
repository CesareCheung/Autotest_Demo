#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


# open()函数

"""
"+"：可以同时读写某个文件，具体为：
r+：读写
w+：写读
x+：写读
a+：写读

w：写文件

"""
# with open('file.json', 'w') as f:
#
# 	f.writelines(temp)


# 文件序列化，把服务器内容写入到文件中

import json

temp = {
	"name": "zhangsan",
	"class": "english",
	"age": "15"
}
json.dump(temp, open('file.json', 'w'))
