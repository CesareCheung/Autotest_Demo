#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

"""
服务端根据请求头中的Content-Type字段来获取消息主体的编码方式
Content-Type:
application/json                  ---->使用data，也可使用json
application/x-www-form-urlencoded ---->使用json,json格式的字符串数据类型

"""
import requests


data={
	"sv": 200,
	"tid": "gda",
	"tv": "r20200810",
	"st": "env"
	      }

header={"Content-Type":" application/json; charset=UTF-8"}
url="https://pagead2.googlesyndication.com/getconfig/sodar"

r=requests.get(url=url,json=data)
print(r.text)

"""
使用json传参时必须满足的要求：
1、Content-Type：application/json
2、请求参数必须为字典
但2必须在1的前提下才可以
"""