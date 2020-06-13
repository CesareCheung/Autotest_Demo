#! usr/bin/env python
# coding=utf-8
# Author="张维序"
class Login:

    def login_test(username, password):
        """
        登录
        :param username:
        :param password:
        :return:
        """
        if username == "Cesare" and password == "123456":
            return True
        else:
            return False

    def profile(login_test):
        """
        登录校验
        :param login_test:
        :return:
        """
        if login_test:
            return "登录成功"
        else:
            return "登录失败"


if __name__ == '__main__':
    pd = Login.login_test("Cesare", "123456")
    print(Login.profile(pd))

# print(profile(login_test("Cesare", "123456")))
