#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


import requests

r = requests.request(
	method="GET",
	url="http://httpbin.org/get"
)
print(r.text)

r = requests.get(
	url="http://httpbin.org/get",
	params=None)

print(f"请求地址：{r.url}")
print(f"响应头：{r.headers}")
print(f"Json格式的数据：{r.json()}")
print(f"基于文本格式的数据：{r.text}")
print(f"二进制的内容：{r.content}")
print(f"状态：{r.status_code}")
print(f"cookies：{r.cookies}")
