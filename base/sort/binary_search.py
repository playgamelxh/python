#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 二分查找算法
@Time: 2019/10/11 11:37 上午
@Author: lvxh
"""

a = [1, 2, 3, 6, 8, 9, 10, 30, 50, 60, 64, 82, 91, 100]

# 二分查找算法
def binary_search(arr, search):
    length = len(arr)
    if length >= 2:
        mid = int(len(arr)/2)
    else:
        if (arr[0] == 'search'):
            return True
        else:
            return False

    if (arr[mid] == search):
        return True
    elif (arr[mid] > search):
        arr = arr[:mid]
        return binary_search(arr, search)
    elif (arr[mid] < search):
        arr = arr[mid:]
        return binary_search(arr, search)

print(binary_search(a, 199))