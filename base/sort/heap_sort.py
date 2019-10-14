#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 堆排序
@Time: 2019/10/12 11:47 上午
@Author: lvxh
"""
import random

a = []
num = 10

for i in range(num):
    a.append(random.randint(1, 100))

# a = [34, 77, 67, 68, 72, 28, 98, 2, 33, 95]
print(a)

# 堆排序主流程
def heap_sort(arr, n, i):
    left = 2*i+1
    right= 2*i+2
    largest = i

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap_sort(arr, n, largest)

# 构建堆
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heap_sort(arr, n, i)
    return arr

print(heapSort(a))

# 一个个交换元素
n = len(a)
for i in range(n - 1, 0, -1):
    a[i], a[0] = a[0], a[i]  # 交换
    heap_sort(a, i, 0)
print(a)