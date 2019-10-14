#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 选择排序
@Time: 2019/10/11 3:57 下午
@Author: lvxh
"""

import random

a = {}
num = 10

for i in range(num):
    a[i] = random.randint(1, 100)

print(a)
# del a[2]
# print(a)

def chose_sort(arr):
    a = []

    while len(arr) > 0:
        min = None
        min_k = None
        for k,v in arr.items():
            if (min == None):
                min = v
                min_k = k
            if (v < min):
                min = v
                min_k = k
        a.append(min)
        del arr[min_k]

    return a

print(chose_sort(a))