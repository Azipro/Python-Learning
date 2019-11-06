# s = "abcdef"
# print(s[1:3])
# print(s[3:10])
# print(s[8:2])
# print(s[:])
# print(s[:2])
# print(s[::2])
# print(s[::-1])
#
#
#
#
# t = ('a','e','i','o','u')
# print(t[-2:-1])
# print(t[-2:])
# print(t[-99:-5])
# print(t[-99:-3])
# print(t[::])
# print(t[1:-1])
# print(t[1::2])
#
#
#
#
# lst = [1,2,3,4,5]
# print(lst[:2])
# lst[:1] = []
# print(lst)
# print(lst[:2])
# lst[:2] = 'a'
# lst[1:] = 'b'
# print(lst)
# del lst[:1]
# print(lst)
#
#
# x = [3, 5, 7]
# x[1:] = [2]
# print(x)
#
# x = [3, 5, 7]
# x[:3] = [2]
# print(x)
#
# numbers = {}
# numbers[(1,2,3)] = 1
# numbers[(1,2)] = 2
# numbers[(2,1)] = 3
# sum = 0
# for k in numbers:
#     sum += numbers[k]
#     print(len(numbers), '', sum, '', numbers)
#

# import jieba
# s = "中国70周年"
# print(jieba.lcut(s))



# fo = open("price2016.csv","r")
# ls = []
# for line in fo:
#     line = line.replace("\n", "")
#     ls = line.split(",")
#     lns = ""
#     for s in ls:
#         lns += "{}\t".format(s)
#     print(lns)
# fo.close()


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