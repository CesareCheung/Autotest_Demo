#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

import requests

data={
	"sv": 200,
	"tid": "gda",
	"tv": "r20200810",
	"st": "env"
	      }

header={"Content-Type":" application/json; charset=UTF-8"}
url="https://pagead2.googlesyndication.com/getconfig/sodar"

r=requests.get(url=url,params=data)
print(r.text)