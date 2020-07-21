#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序
import requests

import json

"""
序列化：把python数据类型转化成str的类型的过程
反序列化：把str类型转化成python数据类型的数据结构
"""
dict1 = {
	"code": "1",
	"msg": "供货厂商列表",
	"data":
		{
			"stores_id": 1,
			"stores_name": "厂商用户1"
		}

}
# print(type(dict1))
url = "https://saasapi.zhaoliangji.com/login"
data = {"phone": "13554143211", "login_type": 2, "password": "zlj123456789", "sms_code": ""}
print(type(data))
# data=json.dumps(data)
header = {"content-type": "application/json"}
login = requests.post(url, data, header)
print(login.json())

# 序列化： dict--->str
dict_str = json.dumps(dict1)
print(dict_str, type(dict_str))

# 反序列化：str--->dict

str_dict = json.loads(dict_str)
print(str_dict, type(str_dict))

list1 = ['weixu', 'class']
print(type(list1))

# 列表的序列化---转换为字符串str
list_str = json.dumps(list1)
print(list_str, type(list_str))

# 列表的反序列化---转换为Python数据类型---转换为列表
str_list = json.loads(list_str)
print(str_list, type(str_list))

# 元组的序列化与反序列化过程
tuple1 = ("a", "b", "c")
print(type(tuple1))

# 元组的序列化
tuple_str=json.dumps(tuple1)
print(tuple_str,type(tuple_str))

# 元组的反序列化---list
str_tuple=json.loads(tuple_str)
print(str_tuple,type(str_tuple))
