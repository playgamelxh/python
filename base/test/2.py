#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/9/28 11:17 上午
@Author: lvxh
"""
import calendar
import datetime

print("Nine-Nine-Multiplication table")
for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}x{1}={2}\t".format(i, j, i*j), end="")
    print("")

print("Fobonacii number")
def fobonacci(n):
    a, b = 0, 1
    k = 1;
    while k <= n:
        print("{0}\t".format(a), end='')
        a, b = b, a+b
        k += 1


fobonacci(10)
print()

print("Armstrong number")
def is_armstrong_number(n):
    a = n
    digits = len(str(a))
    # print(digits)
    num = 0
    while a:
        if (a < 0) :
            break
        a, i = int(a/10), a%10
        num += i**digits
    # print(num)
    if (num == n):
        return True
    else:
        return False

# a = is_armstrong_number(1)
# print(a)
for i in range(1000):
    if (is_armstrong_number(i)):
        print(i,"\t",end='')
print()

a = 10
print("十进制：{0},二进制为：{1}，八进制为：{2}，十六进制为：{3}".format(a, bin(a), oct(a), hex(a)))

a = 'A'
print("字符{0}对应的ASCII码：{1}".format(a, ord(a)))

a = 65
print("ASCII码{0}对应的字符为：{1}".format(a, chr(a)))

def max_common_divisor(a, b):
    small,big = min(a, b), max(a, b)

    ret = 1
    for i in range(1, small+1):
        if (a % i == 0 and b % i == 0) :
            ret = i
    return ret

a,b = 6, 24
print("{0} {1}的最大公约数为:{2}".format(a, b, max_common_divisor(a, b)))

def min_common_multiple(a, b):
    large = max(a, b)
    while True:
        if ((large % a == 0) and (large % b == 0)):
            break
        else:
            large += 1
    return large

a, b = 4, 6
print("{0} {1}的最小公倍数为：{2}".format(a, b, min_common_multiple(a, b)))

yy = 2019
mm = 10
print(calendar.month(yy, mm))

print("递归生成fobonicc数列")

def recursive_fibonacci_sequence(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (recursive_fibonacci_sequence(n-1) + recursive_fibonacci_sequence(n-2))

# print("{0}\t".format(recursive_fibonacci_sequence(5)), end='')
for i in range(1, 10):
    print("{0}\t".format(recursive_fibonacci_sequence(i)), end='')
print()

print("文件IO")
with open("test.txt", 'wt') as out_file:
    out_file.write("写入一段文字")

with open("test.txt", 'rt') as in_file:
    print(in_file.read())

print("当前日期：{0}".format(datetime.date.today()))
print("当前日期：{0}".format(datetime.datetime.now()))

print("约瑟夫生死者小游戏")
people = {}
for i in range(1,31):
    people[i] = 1
print(people)

i,j = 0,0
while i<15:
    for k,v in people.items():
        # print(k, v)
        if (v == 1):
            j += 1
            if (j == 9):
                people[k] = 0
                j = 0
                i += 1
                print("{0}号下船".format(k))


