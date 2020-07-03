#! usr/bin/env python
# coding=utf-8
# Author="张维序"
import requests


def login(url, data, ):
    """
    登录
    :param username:
    :param password:
    :return:
    """
    data = requests.post(url, data)
    return data


