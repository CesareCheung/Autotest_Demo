#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


"""
pytest命令详解：

-v：输出详细的信息
-s：输出测试函数或者测试方法里面的print()里面的内容
-k：按分类执行测试点  -k "对应装饰器" 如： -k "login or ui"
-m：进行分组  如： -m "login or ui"

"""
import  pytest
def test_userid():
	userid=123
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