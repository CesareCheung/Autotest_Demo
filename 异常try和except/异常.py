#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


def div(a, b):
	return a / b


"""
1、try 执行代码正常，就不会执行expect代码
2、只有try代码执行异常，就会执行expect的代码
"""

# try:
# 	div(1, 0)
# except ZeroDivisionError as e:
# 	print(e.args)
# except ValueError as e:
# 	print(e.args)
# except KeyError as e:
# 	print(e.args)

# Exception 所有异常类型

try:
	div(1,0)
except Exception as e:
	print(e)