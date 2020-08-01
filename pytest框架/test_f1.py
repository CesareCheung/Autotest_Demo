#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序



"""
在pytest的测试框架中，它的搜索规则是：
在一个被执行的目录下，寻找以test开头或者以test结尾的测试模块，然后执行
里面以test开头的测试方法或者测试函数
"""
import pytest

def test_001():
    assert 1==1

def test_004():
    pass

def test_002():
    assert 1!=2

def test_003():
    pass


class TestF1:
    def test_001(self):
        pass


if __name__ == '__main__':
    pytest.main(["-v"])