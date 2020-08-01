#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序
import json
import sys


class Login():
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def getUsername(self):
		return self.username

	def setUsername(self, name):
		self.username = name

	def getPassword(self):
		return self.password

	def setPassword(self, passwd):
		self.password = passwd

	def register(self):
		temp=self.username+"|"+self.password
		json.dump(temp,open('login.json','w'))
		print("恭喜你注册成功！")

	def login(self):
		f=str(json.load(open('login','r')))
		list1=f.split('|')
		if list1[0]==self.username and list1[1]==self.password:
			return True
		else:
			return False
	def userinfo(self):
		f=str(json.load(open('login.json','r')))
		list1=f.split('|')
		r=self.login()
		if r:
			print(f"恭喜进入系统{list1[0]}")
		else:
			print("登录失败，请重新检查账号是否正确！")
	def exit(self):
		sys.exit()

def main():
	"""
	主运行函数
	:return:
	"""
	per=Login("zhangsan",'123456')
	while True:
		try:
			t=int(input("1、注册，2、登录，3、退出系统"))
		except Exception as e:
			print(e.args)
		else:
			if t==1:
				per.register()
			elif t==2:
				per.userinfo()
			elif t==3:
				per.exit()
			else:
				print("请输入正确数字！")
		finally:
			pass

if __name__ == '__main__':
	main()
