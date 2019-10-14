#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 快速排序
@Time: 2019/10/11 2:58 下午
@Author: lvxh
"""

import random

a = []
num = 10

for i in range(num):
    a.append(random.randint(1, 100))

print(a)

def quick_sort(arr):

    if (len(arr) >= 2):
        a = []
        b = []
        base = arr[0]
        for i in range(1, len(arr)):
            if arr[i] <= base:
                a.append(arr[i])
            else:
                b.append(arr[i])
        a = quick_sort(a)
        b = quick_sort(b)
        return a+[base]+b
    else:
        return arr

print(quick_sort(a))
