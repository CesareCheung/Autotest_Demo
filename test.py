#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:序

# 查看内置方法dir()
str1 = "admin"
print(dir(str1))
# replace替换字符串
print(str1.replace('ad', 'baidu'))

# 列表
# 列表中的方法
print(dir(list))

"""
 'append':末尾追加
 'clear'：
 'copy'：复制列表
 'count'：列表中元素出现的次数
 'extend'：将列表合并到对应列表
 'index'：对应元素第一次出现的索引
 'insert'：插入，带索引 
 'pop'：默认删除最后一位并打印出来
 'remove'：删除，对应对象中不再包含对应元素
 'reverse'：反转排序
 'sort':从小到大的排序
"""
list1 = [1, 99, 23, 45, 99, 44]
print(list1.count(99))
print(list1.index(99))
list1.remove(1)
print(list1)

list1.pop()
print(list1)

list2 = [1, 99, 22, 34, 45]
list1.extend(list2)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)

# 字典

dict1 = {"name": "zhangsan", "age": 18}
dict2 = {"adr": "shenzhen"}
# items()--->整个字典循环，输出对应的所有key和value
for key, value in dict1.items():
    print(key, value)
print(dir(dict))

# update--->更新
dict1.update(dict2)
print(dict1)

# 字典取值
data= {"pay_apply_id": 76, "pay_apply_no": "BM202004297680186", "order_no": "B20200429107147381", "business_id": 53}

for key,value in data.items():
    if key =="pay_apply_id":
        print(key, ":", value)