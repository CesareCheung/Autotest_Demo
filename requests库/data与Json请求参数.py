#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

"""
服务端根据请求头中的Content-Type字段来获取消息主体的编码方式
Content-Type:
application/json                  ---->使用data，也可使用json
application/x-www-form-urlencoded ---->使用json,json格式的字符串数据类型

"""