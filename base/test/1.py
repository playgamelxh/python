#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/9/27 8:33 上午
@Author: lvxh
"""
import cmath
import random

print("Hello World!")

print("求数字之和")
a = 1
b = 2
def sum(a, b):
    return a+b
print("a+b:",sum(a, b));

print("9的平方根为：", 9**0.5)

a = -9
num = cmath.sqrt(a)
print("{0}的平方根：实部为：{1:0.3f}, 虚部为：{2:0.3f}j".format(a, num.real, num.imag));

a = 3
b = 4
c = 5
d = (a+b+c)/2
print("边长{0}，{1}，{2}三角形面积:{3:0.3f}".format(a, b, c, (d*(d-a)*(d-b)*(d-c))**0.5))

r = 3
print("半径{0},计算圆的面积:{1}".format(r, cmath.pi * r ** 2))
print(cmath.pi)

a = 1
b = 10
print("生成{0}到{1}随机数：{2}".format(a, b, random.randint(a, b)));

dict = {'0': 5, '1': 10, '2': 20, '3': 50, '4': 100}
print(dict.get('0', 500))

celsius = 37.5
print("摄氏温度：{0}℃,华氏温度为：{1:.2f}F".format(celsius, celsius*1.8+32))

x, y = 1, 2
print("{0} {1}".format(x, y))
x, y = y, x
print("交换后为{0} {1}".format(x, y))

def is_leap_year(year):
    if (year % 4 == 0) :
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("{0}是闰年".format(year))
            else:
                print("{0}不是闰年".format(year))
        else:
            print("{0}是闰年".format(year))

    else:
        print("{0}不是闰年".format(year))

is_leap_year(2000)
is_leap_year(2011)
is_leap_year(2100)

a = (1,2)
print(max(a))
b = [1,2]
print(max(b))
c = {1, 2, 3}
print(c)
d = {"1":1, "2":2, "3":3}
print(max(d))