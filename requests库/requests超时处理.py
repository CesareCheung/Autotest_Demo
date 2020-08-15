#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

"""
固定时间--->>>timeout 超时时间
"""

import requests

r=requests.get("http://httpbin.org/get",timeout=1)

print(r.text)