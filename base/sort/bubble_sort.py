#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 冒泡排序
@Time: 2019/10/11 4:37 下午
@Author: lvxh
"""

import random

a = []
num = 10

for i in range(num):
    a.append(random.randint(1, 100))

print(a)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(bubble_sort(a))