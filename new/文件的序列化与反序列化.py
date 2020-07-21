#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

import json
import requests

"""
文件的序列化与反序列化


"""

r = requests.get(url="http://www.weather.com.cn/data/sk/101190408.html")
# print(r.content.decode("utf-8"))

# 文件序列化--->把服务端的响应数据写到文件中
json.dump(r.content.decode("utf-8"), open("weather.json", "w"))



"""
1、文件反序列化后,类型是unicode
2、进行编码，把Unicode类型转换为str类型
3、然后使用反序列化把str转换为字典类型
"""
# 文件的反序列化--->读取文件内容
fp=json.load(open("weather.json", "r"))
print(fp,type(fp))

# 把读取的数据进行反序列化
dict1=json.loads(fp)
print(type(dict1),dict1['weatherinfo']['city'])

