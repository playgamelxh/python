#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 尾递归
@Time: 2019/9/28 10:42 上午
@Author: lvxh
"""

# 普通递归函数
def recursion(n):
    if (n == 1):
        return 1
    else:
        return n * recursion(n-1)

# 尾递归函数
def tail_recursion(n, total=1):
    if (n == 1):
        return total
    else:
        return tail_recursion(n-1, total*n)

# python3递归上限999
a = 998
print("{0}的阶乘尾：{1}".format(a, recursion(a)))
print("{0}的阶乘尾：{1}".format(a, tail_recursion(a)))