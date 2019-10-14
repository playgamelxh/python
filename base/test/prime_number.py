#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 输出质数
@Time: 2019/9/28 10:35 上午
@Author: lvxh
"""

def is_prime_number(n):

    if (n <= 0):
        return False
    n = int(n)

    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

for i in range(100):
    if (is_prime_number(i)):
        print("{0} is prime number".format(i))