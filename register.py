#! usr/bin/env python
# coding=utf-8
# Author="张维序"

"""
1、注册账户
2、登录账户
3、获取昵称
"""


def inOut():
    """
    输入数据
    :return:
    """
    username = input("请输入账号：\n")
    password = input("请输入账号密码：\n")
    return username, password


def register():
    """
    实现账号注册功能
    :return:
    """
    username, password = inOut()
    temp = username + "|" + password
    with open(".\login.md", 'w+') as fp:
        fp.write(temp)


register()


def login():
    """
    实现登录账号
    :return:
    """
    username, password = inOut()
    with open(".\login.md", "r") as fp:
        info = fp.read()
        info = info.split("|")  # 字符串切割成列表
        print(info)
        if username == info[0] and password == info[1]:
            return True
        else:
            return False


print(login())


def getNick(func):
    """
    获取昵称
    :return:
    """
    with open(".\login.md", 'r') as fp:
        info = fp.read()
        info = info.split("|")
        if func:
            print(f"{info[0]}，欢迎您")
        else:
            print("请登录系统")


getNick(login())

if __name__ == '__main__':

    while True:
        t = int(input("1、注册2、登录3、退出"))
        if t == 1:
            register()
        elif t == 2:
            getNick(login())
        elif t == 3:
            import sys

            sys.exit(1)
        else:
            print("输入错误，请继续")
            continue
