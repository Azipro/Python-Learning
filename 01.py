""" 纸币转换
val = input()
if val[-1] in ['$']:
    x = 6 * float(val[0:-1])
    print("%.2f￥"%x)
elif val[-1] in ["￥"]:
    y = float(val[0:-1]) / 6
    print("%.2f$"%y)
else:
    print("error")
"""






""" 画图1.0
import turtle
turtle.setup(650,350)
turtle.hideturtle()
turtle.up()
turtle.goto(-100,-70)
turtle.pensize(2)
turtle.pd()
for i in range(0,3):
    turtle.seth(i*120)
    turtle.fd(200)
turtle.up()
turtle.seth(60)
turtle.fd(100)
turtle.pd()
for i in range(0,3):
    turtle.seth(i*(-120))
    turtle.fd(100)
turtle.done()
"""

""" 画图2.0
import turtle
turtle.setup(650,350)
turtle.up()
turtle.goto(-100,-70)
turtle.pensize(2)
turtle.pd()
for i in range(0,3):
    turtle.seth(i * 120)
    turtle.fd(100)
    if i in[0, 1]:
        for j in range(0,3):
            turtle.seth(j * 120)
            turtle.fd(100)
turtle.done()
"""





"""
from math import *
x = 0.01
dayup = pow((1.0 + x) , 365)
daydown = pow((1.0 - x) , 365)
print("向上: %.2f, 向下: %.2f."%(dayup, daydown))

dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("向上5天，向下2天的力量：%.2f"%dayup)

def dayUP(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup *(1 + df)
    return dayup

x = 0.01
while(dayUP(x) < 37.78):
    x += 0.001

print("每天的努力参数是: %.3f"%x)
"""





"""
x = eval(input())
print("fat" if x >= 200 else "not fat")
"""

"""
#1
from random import *
for i in range(10):
    print(randint(0, 100))

#2
from random import *
while 1:
    x = randint(0, 100)
    if x % 2 != 0:
        print(x)
        break

#3
for i in range(4):
    print(choice("abcdefghij"))

#4
print(choice(["apple", "pear", "peach", "orange"]))
"""






"""
from random import *
from math import *
#from time import *
DARTS = 1000000
hits = 0.0
#clock()
for i in range(1, DARTS + 1):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
print("PI的值是:%.5f"%pi)
#print("运行时间是:{:.5f}s".format(clock()))
"""




"""
try:
    alp = "QWERTYUIOPASDFGHJKLZXCVBNM"
    idx = eval(input())
    print((alp[idx]))
except NameError:
    print("输入错误!")
else:
    print("没有发生异常!")
finally:
    print("程序执行完毕，不知道是否发生异常!")
"""



"""
import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print(final)
"""


"""
import datetime
bri = datetime.date(1999,4,30)
#1
print(bri.isoformat())
#2
print(bri.__format__("%Y/%m/%d"))
#3
print(bri.__format__("%D"))
#4
print(bri.strftime("%Y%m%d"))
#5
print(bri.ctime())
"""


# def Ers(a1, q, n):
#     if n == 1:
#         return a1
#     else:
#         return eval("a1 * q ** (n - 1)") + Ers(a1, q, n - 1)
#
# a1 = eval(input())
# q = eval(input())
# n = eval(input())
#
# result = Ers(a1, q, n)
# print(result)



# #gcd
# def gcd(x, y):
#     return x if y==0 else gcd(y, x%y)
#
# print(gcd(10,20))


# def judge(para1, **para2):
#     print(type(para2))
#
#     print(para2)
# judge(1, a=2, b=3, c=4, d=5)


# dic = {"a" : "sa", "b" : "as"}
# dic["s"] = "sad"
# for i in dic:
#     print(i)
#     print(dic[i])

# txt = open("a.txt", "r", encoding="utf-8").read()
# # for i in txt:
# #     with open("b.txt", "a", encoding="utf-8") as wr:
# #         wr.write(i)


# tup1 = (1, 2, 3, 4, 5)
# list2 = [6,7,8,9,10]
# dict3 = {'name':'xiaoming','sex':'man','age':'20'}
# str4 = 'Hello World'
#
# print("".join(map(str, tup1))) #元组转字符串
# print(list(tup1)) #元组转列表
# print(dict(zip(tup1[0::1], tup1[1::1]))) #元组转字典
#
#
# print(str(list2)) #列表转字符串
# print(tuple(list2))  #列表转元组
# print(dict(zip(list2[0::1], list2[1::1])))  #列表转字典
#
# print(str(dict3)) #字典转字符串
# print(tuple(dict3))  #字典转元组
# print(list(dict3))  #字典转列表
#
# print(list(str4)) #字符串转列表
# print(tuple(str4)) #字符串转元组
# print(dict(zip(str4[0::1], str4[1::1]))) #字符串转字典