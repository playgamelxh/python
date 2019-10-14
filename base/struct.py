#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/9/26 10:11 下午
@Author: lvxh
"""

print("列表当做堆栈")
list = []
list.append(1)
list.append(2)
print(list)
list.pop()
print(list)
list.pop()
print(list)

print("列表当做队列")
queue = []
queue.append(1)
queue.append(2)
print(queue)
a = queue.pop(0)
print(a, queue)
a = queue.pop(0)
print(a, queue)

print("列表推导式")
vec = [1, 2, 3]
b = [3*x for x in vec]
print(vec, b)

print('嵌套列表解析')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
b = [[row[i] for row in matrix] for i in range(4)]
print(b)

c = []
for i in range(4):
    c.append([row[i] for row in matrix])
print(c)

print("元组")
t = 'a', 'b', 'c'
print(t)
t = ('a', 'b', 'c')
print(t)

print("集合")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
set = set()
print(set)

print('字典')
a =  dict(sape=4139, guido=4127, jack=4098)
print(a)