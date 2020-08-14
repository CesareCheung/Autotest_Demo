#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


import requests

# get请求
params = {"word": "无涯", "pobook": 0}

url = "https://yuedu.baidu.com/search"

r = requests.get(url=url, params=params)

print(r.content.decode("gbk"))
print(r.url)

# post请求

url="http://httpbin.org/post"

data={"name":"Cesare","age":28}

r=requests.post(url=url,data=data)

print(r.json())
