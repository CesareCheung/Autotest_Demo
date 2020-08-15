#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序
import json

import requests

"""
请求参数中字典里面包含列表，列表中又包含字典： "data": "[{'type_id':23}]"
"""
url = "www.wuya.com"
datas = {"name": "wuya", "age": 29, "data": "[{'type_id':23}]"}
headers = {"Content-type": "application/json"}   #---->>>json格式字符串--->>>str

# 对对应数据进行序列化处理
datas['data']=json.dumps(datas['data'])

r=requests.post(url=url,json=datas,headers=headers)