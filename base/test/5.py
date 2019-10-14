#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/10/13 3:05 下午
@Author: lvxh
"""

#! /usr/bin/python

a = "Hello World! This is Tom."
print(a)
# 颠倒字符串
def reverse_words(str):
    length = len(str)
    temp = ''
    j = 0
    for i in range(length):
        if str[length-1-j] == ' ':
            temp += ' '
            print(temp)
            str = temp + str[:length-len(temp)]
            print(str)
            temp = ''
            j = 0
        else:
            temp = str[length-1-j] + temp
            j += 1
    temp += ' '
    # print(temp, str)
    str = temp + str[:length - len(temp)]
    return str

# 颠倒字符串
def reverse_str(str):
    str_len = len(str)
    i, j = 0, 0
    temp, c = '', ''
    while i < str_len:
        # print(str, str_len-1-j)
        c = str[str_len-1-j]
        if c == ' ':
            temp += ' '
            j += 1
            # print("拼接：temp", temp, "开头：",str[:i], "结尾：",str[i:str_len-j])
            str = str[:i] + temp + str[i:str_len-j]
            # print("结果：", str)
            j = 0
            i += len(temp)
            temp = ''
        else:
            temp = c + temp
            j += 1

    return str

# print(reverse_words(a))
print(reverse_str(a))

# print(a[2])
# a[0],a[1]=a[1],a[0]
# a = list(a)
# print(a)
