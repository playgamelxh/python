#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 归并排序
@Time: 2019/10/11 5:17 下午
@Author: lvxh
"""

import random

a = []
num = 10

for i in range(num):
    a.append(random.randint(1, 100))

# a = [34, 77, 67, 68, 72, 28, 98, 2, 33, 95]
print(a)

def merge_sort(arr):

    if (len(arr) >= 2):
        mid = int(len(arr)/2)
        a = arr[:mid]
        b = arr[mid:]

        # print("排序前", a, b)
        a = merge_sort(a)
        b = merge_sort(b)
        # print("排序后", a, b)
        # 归并排序
        ret = []
        aa, bb = None, None
        while len(a) > 0 or len(b) > 0:
            if aa == None and len(a) > 0:
                aa = a.pop(0)
            if bb == None and len(b) > 0:
                bb = b.pop(0)

            if (aa == None and bb != None):
                ret.append(bb)
                bb = None
            if (aa != None and bb == None):
                ret.append(aa)
                aa = None
            if (aa != None and bb != None):
                if (aa <= bb):
                    ret.append(aa)
                    aa = None
                else:
                    ret.append(bb)
                    bb = None
        if aa != None:
            ret.append(aa)
        if bb != None:
            ret.append(bb)

        # print("ret", ret)
        return ret
    else:
        # print("arr长度小于2", arr)
        return arr

print(merge_sort(a))
# print(a[:5])
# print(a[5:])
# print(a.pop(0))
# print(a.pop(0))
# print(a.pop(0))
# for i in a:
#     print(i)