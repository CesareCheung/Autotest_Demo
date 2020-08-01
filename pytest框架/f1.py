#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序


# pytest框架定义函数必须以test开头

import pytest

def test_001():
    assert 1==1

def test_002():
    assert 1==2




class TestF1:
    def test_001(self):
        pass


if __name__ == '__main__':
    pytest.main(["-v","f1.py"])