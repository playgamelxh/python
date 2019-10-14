#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 描述
@Time: 2019/10/12 4:15 下午
@Author: lvxh
"""
import re

a = 'www.baidu.com'
print(re.match('www', a))
print(re.match('www', a).span())
print(re.match('com', a))

print(re.search('www', a))
print(re.search('www', a).span())
print(re.search('com', a).span())

print(re.sub('www.', '', a))

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
print(matchObj)
print(matchObj.group())
print(matchObj.group(1))
print(matchObj.group(2))