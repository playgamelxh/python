#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-

"""
@desc: 基础实例
@Time: 2019/10/9 8:43 上午
@Author: lvxh
"""
import time
import re
import datetime

# print('按下回车开始计时，按下 Ctrl + C 停止计时。')
# while True:
#     try:
#         input()
#         print('开始')
#         st = time.time()
#         while True:
#             print("{}".format(int(time.time()-st)))
#             time.sleep(1)
#
#     except KeyboardInterrupt:
#         print('结束')

# 计算N个自然数的立方和
def numCubeSum(n):
    num = 0
    for i in range(1, n+1):
        num += i**3
    return num

n = 5
print("{0}到{1}的立方和为：{2}".format(1, n, numCubeSum(n)))

a = {1, 2, 3, 4, 5}
print(sum(a))

b = [1, 2, 3, 4, 5]
print(sum(b))

# 列表左移
def moveLeft(arr, n):
    while n > 0:
        temp = arr[0]
        print(temp)
        if (len(arr) < 2):
            pass
        else:
            for i in range(0, len(arr)-1):
                arr[i] = arr[i+1]
            arr[len(arr)-1] = temp
            n -= 1
    return arr

a = [1, 2, 3, 4, 5, 6]

print(moveLeft(a, 3))

# 对调列表头尾两个元素
def headToTail(list):
    last = len(list)-1
    # temp = list[0]
    # list[0] = list[last]
    # list[last] = temp
    list[0], list[last] = list[last], list[0]
    return list

a = [1, 2, 3, 4, 5, 1]
print(a)
print(headToTail(a))

print(list(reversed(a)))
print(tuple(reversed(a)))
print(set(reversed(a)))

t = 1
if t in a:
    print("{0} in {1}".format(t, a))
else:
    print("{0} not in {1}".format(t, a))

print(a.count(1))

a.sort()
print(a)
print(min(a))
b = (1, 2, 3)
print(min(b))
c = {1, 2, 3}
print(min(c))

a,b="aaaa","bbbb"
print(a+b)

a,b="aaaabbbbbbaaaaa",'aaabb'
print(a.find(b))

a = "http://c.xingkuang.com/abdc/defe"
print(re.findall('http://.+', a))

def findUrl(string):
    url = re.findall("https?://[.\w]+", string)
    return url
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：http://www.google.com'
print("Urls: ", findUrl(string))

def exec_code():
    code = """
print("123")
"""
    exec(code)

exec_code()

print('翻转字符串')
a = 'abcdefg'
print(a[::-1])
print(''.join(reversed(a)))

key_value = {}

key_value[3] = 323
key_value[1] = 2
key_value[2] = 56
key_value[4] = 30

# print(sorted(key_value.items()))
print(sorted(key_value.items(), key = lambda k:(k[1], k[0])))

a={'0':'a', '1':'b', 'a':'aaa', 'b':'bbb'}
print(a)
del a['1']
print(a)
print(a.pop('b'))
print(a)
b = {key:val for key, val in a.items() if key != '0'}
print(b)

a = {'0':0, '1':1}
b = {'a':'a', 'b':'b'}
# a.update(b)
# print(a)
print({**a, **b})

a = "2019-10-11 12:00:00"
timeArray = time.strptime(a, '%Y-%m-%d %H:%M:%S');
print(a)
b = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
print(b)
timStamp = int(time.mktime(timeArray))
print(timStamp)

a = datetime.timedelta(days = 3)
print("a",a)
threeDayAgo = datetime.datetime.now() - a
print(datetime.datetime.now())
print(threeDayAgo)
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
print(timeStamp)
print(threeDayAgo.strftime('%Y-%m-%d %H:%M:%S'))

print(time.time())
print(time.localtime())

