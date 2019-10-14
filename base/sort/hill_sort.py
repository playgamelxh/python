#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 希尔排序
@Time: 2019/10/12 2:23 下午
@Author: lvxh
"""
import random

a = []
num = 10

for i in range(num):
    a.append(random.randint(1, 100))

print(a)

# 希尔排序
def hill_sort(arr):
    # 每次区间跨度为一半
    n = len(arr)
    span = int(n/2)
    while span > 0:
        print(span)
        for i in range(0, n-span):
            # 循环，插入到指定位置
            j = i+span
            while j < n:
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                j += span
            pass
        print(arr)
        # 更改跨度
        span = int(span/2)

    return arr

print(hill_sort(a))