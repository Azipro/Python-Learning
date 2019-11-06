s = "abcdef"
print(s[1:3])
print(s[3:10])
print(s[8:2])
print(s[:])
print(s[:2])
print(s[::2])
print(s[::-1])



t = ('a','e','i','o','u')
print(t[-2:-1])
print(t[-2:])
print(t[-99:-5])
print(t[-99:-3])
print(t[::])
print(t[1:-1])
print(t[1::2])




lst = [1,2,3,4,5]
print(lst[:2])
lst[:1] = []
print(lst)
print(lst[:2])
lst[:2] = 'a'
lst[1:] = 'b'
print(lst)
del lst[:1]
print(lst)


x = [3, 5, 7]
x[1:] = [2]
print(x)

x = [3, 5, 7]
x[:3] = [2]
print(x)


numbers = {}
numbers[(1,2,3)] = 1
numbers[(1,2)] = 2
numbers[(2,1)] = 3
sum = 0
for k in numbers:
    sum += numbers[k]
    print(len(numbers), '', sum, '', numbers)


import jieba
s = "中国70周年"
print(jieba.lcut(s))



fo = open("price2016.csv","r")
ls = []
for line in fo:
    line = line.replace("\n", "")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()



import sqlite3
con = sqlite3.connect("content.db")
cur = con.cursor()
print("创建成功！")
while True:
    print("==================================================")
    print("1.新建     2.查找    3.添加    4.修改    5.删除    6.排序    0.退出")
    print("==================================================")
    choice = int(input("请输入你的选择(0-6):"))
    if choice == 0:
        break
    elif choice < 0 or choice > 6:
        print("非法输入！请重新输入！")
        continue
    elif choice == 1:
        sqlstr = """
                create table myaddr(
                        id int primary key not null,
                        name text not null,
                        tel text not null,
                        addr text
                );
        """
        cur.execute(sqlstr)
        print("创建成功！")
    elif choice == 2:
        seKey = input("请输入要查找的关键字(*代表全部)：")
        if seKey == '*':
            mylist = cur.execute("select * from myaddr")
        else:
            mylist = cur.execute("select id, name, tel, addr"
                                 "from myaddr where id = ? or name like ?"
                                 "or tel like ? or addr like ?",(seKey.strip(),
                                                                 ("%" + seKey.strip() + "%"),
                                                                 ("%" + seKey.strip() + "%"),
                                                                 ("%" + seKey.strip() + "%"),
                                                                 ("%" + seKey.strip() + "%")))
        for row in mylist:
            print("id = {} name = {} tel = {} addr = {}".format(*row))
    elif choice == 3:
        id = input("请输入id：")
        name = input("请输入name：")
        tel = input("请输入tel：")
        addr = input("请输入addr：")
        sqlstr = """
                insert into myaddr(id, name, tel, addr) values(?,?,?,?)
        """
        cur.execute(sqlstr, (int(id), name, tel, addr))
        con.commit()
        print("添加成功！")
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass

cur.close()



""" 纸币转换"""
val = input()
if val[-1] in ['$']:
    x = 6 * float(val[0:-1])
    print("%.2f￥"%x)
elif val[-1] in ["￥"]:
    y = float(val[0:-1]) / 6
    print("%.2f$"%y)
else:
    print("error")






""" 画图1.0"""
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


""" 画图2.0"""
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




x = eval(input())
print("fat" if x >= 200 else "not fat")



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






from random import *
from math import *
from time import *
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


import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print(final)



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



def Ers(a1, q, n):
    if n == 1:
        return a1
    else:
        return eval("a1 * q ** (n - 1)") + Ers(a1, q, n - 1)

a1 = eval(input())
q = eval(input())
n = eval(input())

result = Ers(a1, q, n)
print(result)



#gcd
def gcd(x, y):
    return x if y==0 else gcd(y, x%y)

print(gcd(10,20))


def judge(para1, **para2):
    print(type(para2))

    print(para2)
judge(1, a=2, b=3, c=4, d=5)


dic = {"a" : "sa", "b" : "as"}
dic["s"] = "sad"
for i in dic:
    print(i)
    print(dic[i])

txt = open("a.txt", "r", encoding="utf-8").read()
# for i in txt:
#     with open("b.txt", "a", encoding="utf-8") as wr:
#         wr.write(i)


tup1 = (1, 2, 3, 4, 5)
list2 = [6,7,8,9,10]
dict3 = {'name':'xiaoming','sex':'man','age':'20'}
str4 = 'Hello World'

print("".join(map(str, tup1))) #元组转字符串
print(list(tup1)) #元组转列表
print(dict(zip(tup1[0::1], tup1[1::1]))) #元组转字典


print(str(list2)) #列表转字符串
print(tuple(list2))  #列表转元组
print(dict(zip(list2[0::1], list2[1::1])))  #列表转字典

print(str(dict3)) #字典转字符串
print(tuple(dict3))  #字典转元组
print(list(dict3))  #字典转列表

print(list(str4)) #字符串转列表
print(tuple(str4)) #字符串转元组
print(dict(zip(str4[0::1], str4[1::1]))) #字符串转字典



#A
n = eval(input())
sum = eval("0")
for i in range(n):
    if i % 2 == 0:
        sum += eval("1 / (i + 1)")
    else:
        sum -= eval("1 / (i + 1)")
print("{:.1f}".format(sum))



#B
for i in range(2):
    val = input()
    if val[-1] in ['D']:
        x = 6.9 * float(val[0:-1])
        print("%.1fR"%x)
    elif val[-1] in ["R"]:
        y = float(val[0:-1]) / 6.9
        print("%.1fD"%y)
    else:
        print("error")



#C
for i in range(2):
    x = input()
    z = reversed(x)
    if list(x) == list(z):
        print("True")
    else:
        print("False")


#D
import math
for i in range(3):
    s = input()
    x = s.split(",")
    a = eval(x[0])
    b = eval(x[1])
    c = eval(x[2])
    if (a + b > c) & (a + c > b) & (b + c > a):
        C = a + b + c
        S = math.sqrt(C / 2 * (C / 2 - a) * (C / 2 - b) * (C / 2 - c))
        print("{:.1f},{:.1f}".format(C, S))
    else:
        print("无法构成三角形！")

