#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 插入排序
@Time: 2019/10/11 1:14 下午
@Author: lvxh
"""
import random

a = []
num = 10

for i in range(num):
    a.append(random.randint(1, 100))

print(a)

def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        current = arr[i]
        while j >=0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

print(insert_sort(a))