#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/9/26 10:46 下午
@Author: lvxh
"""
import sys
import doctest

# 斐波那契(fibonacci)数列模块

def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

dir(fib(3))
dir(sys)
a = 1
b = [2, 3, 4]
dir()

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

doctest.testmod()
# print(a)