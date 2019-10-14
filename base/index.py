#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/9/26 8:01 下午
@Author: lvxh
"""

import sys

a, b = 0, 1
while b < 1000:
    # print(b, end=',')
    # print(b)
    a, b = b, a+b

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count,"大于等于5")

for letter in "abcdefg":
    print(letter)

list = [1,2,3,4]
it = iter(list)
print("迭代器")
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
        # sys.exit();

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print("自定义迭代器")
print(next(myiter))
print(next(myiter))
print(next(myiter))
for i in myiter:
    print(i)

def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if (count > n):
            return
        yield a
        a, b = b, a + b
        count += 1

print("斐波那契：")
for i in fibonacci(5):
    print(i)


print("函数")
print("不可变参数")
a = 1
def funa(b):
    b = 10
    print(b)

funa(a)
print(a)

print("可变参数")
a = [1, 2, 3]
def add(b):
    b.append(4)

add(a)
print(a)

print("元组参数")
def fun1(a, *b):
    print(a)
    print(b)
fun1(1, 2, 3, 4, 5)

print("字典参数")
def fun2(a, **b):
    print(a)
    print(b)
    for key in b:
        print(key, b[key])

fun2(2, b=1,c=2,d=3)

print("匿名函数")
sum = lambda a,b:a+b

print("a+b", sum(1, 2))