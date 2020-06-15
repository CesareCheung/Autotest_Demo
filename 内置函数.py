list1 = [1, 3, 4, 5]

add = list(map(lambda a: a + 100, list1))
print(add)
# map(函数，可迭代的请求参数)：
add = lambda a, b: a + b  # lambda 参数，参数:表达式
print(add(2,4))