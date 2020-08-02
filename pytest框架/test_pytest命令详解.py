#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


"""
pytest命令详解：

-v：输出详细的信息
-s：输出测试函数或者测试方法里面的print()里面的内容
-k：按分类执行测试点  -k "对应装饰器" 如： -k "login or ui"
-m：进行分组  如： -m "login or ui"
-x:执行失败时立即停止
--maxfail:执行失败的最大次数
--tb=no:关闭信息
--tb=short:只输出assert的错误信息
--tb=line:一行展示所有信息，不会提示具体的函数，但会告诉断言失败的代码行数
--If：定位错误
--duration=0:测试函数执行速度
"""
import pytest


def test_userid():
	userid = 123
	print(userid)


@pytest.mark.ui
def test_001():
	pass


@pytest.mark.ui
def test_002():
	pass


class TestUi:
	@pytest.mark.login
	def test_login_001(self):
		pass

	@pytest.mark.login
	def test_login_002(self):
		pass

	@pytest.mark.logout
	def test_logout_001(self):
		pass


if __name__ == '__main__':
	pytest.main(["-v"])

import requests


def test_baidu():
	r = requests.get("http://baidu.com")
	assert r.status_code == 200


def test_taobao():
	r = requests.get("http://taobao.com")
	assert r.status_code == 200


def test_qq():
	r = requests.get("http://qq.com")
	assert r.status_code == 200
