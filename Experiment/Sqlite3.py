import sqlite3
import xlrd

def importXlsx():
    xls = xlrd.open_workbook("Address.xlsx")
    ws = xls.sheet_by_index(0)
    ls = []
    for i in range(ws.nrows):
        ls.append(ws.row_values(i))
    return ls

def createDb(ls):
    con = sqlite3.connect("Address.db")
    cur = con.cursor()
    droptable_sql = "drop table if exists Addr"
    cur.execute(droptable_sql)

    cur.execute("""
                    create table Addr(
                        "id" int not null,
                        "name" text not null, 
                        "tel" int not null,
                        "email" text not null,
                        "address" text not null
                    );
            """)
    for i in range(len(ls) - 1):
        str = "insert into Addr(id, name, tel, email, address) values (?, ?, ?, ?, ?) "
        cur.execute(str, (ls[i + 1][0], ls[i + 1][1], ls[i + 1][2], ls[i + 1][3], ls[i + 1][4]))
    con.commit()
    cur.close()
    con.close()



class AddressBook():
    def __init__(self, con, cur):
        self.con = con
        self.cur = cur

    #查找
    def selectInfo(self):
        key = input("Please input the key：(*)")
        if key == "*":
            info = self.cur.execute("select * from Addr")
        else:
            info = self.cur.execute("select id, name, tel, email, address "
                                    "from Addr where id = ? or name like ? "
                                    "or tel like ? or email like ? or address like ?",
                                    (key.strip(),("%" + key.strip() + "%"),
                                                 ("%" + key.strip() + "%"),
                                                 ("%" + key.strip() + "%"),
                                                 ("%" + key.strip() + "%")))
        for i in info:
            print("{} {} {} {} {}".format(*i))

    #添加
    def insertInfo(self):
        id = input("Please input id：")
        name = input("Please input name：")
        tel = input("Please input tel：")
        email = input("Please input email：")
        address = input("Please input address：")
        str = """
                        insert into Addr(id, name, tel, email, address) values(?,?,?,?,?)
                """
        self.cur.execute(str, [int(id), name, int(tel), email, address])
        self.con.commit()

    #删除
    def deleteInfo(self):
        key = input("Please input the id that you want to delete：")
        info = self.cur.execute("select id, name, tel, email, address "
                                "from Addr where id = ?", (key.strip(),))
        print("-----The infomation you want to delete is：-----")
        for i in info:
            print("{} {} {} {} {}".format(*i))
        self.cur.execute("delete from Addr where id = ?", (key.strip(),))

    #更新
    def updateInfo(self):
        key = input("Please input the id that you want to update：")
        info = self.cur.execute("select id, name, tel, email, address "
                                "from Addr where id = ?", (key.strip(),))
        print("-----The infomation you want to update is：-----")
        for i in info:
            print("{} {} {} {} {}".format(*i))
        print("-----Please input your key and content：(id, name, tel, email, address)-----")
        p = input("Please input name：(if don't update, input '?')")
        if p != "?":
            self.cur.execute("update Addr set name = ? where id = ?", (p, key))
        p = input("Please input tel：(if don't update, input '?')")
        if p != "?":
            self.cur.execute("update Addr set tel = ? where id = ?", (p, key))
        p = input("Please input email：(if don't update, input '?')")
        if p != "?":
            self.cur.execute("update Addr set email = ? where id = ?", (p, key))
        p = input("Please input address：(if don't update, input '?')")
        if p != "?":
            self.cur.execute("update Addr set address = ? where id = ?", (p, key))

def main():
    ls = importXlsx()
    try:
        createDb(ls)
    except Exception as e:
        print("Failed to create the datebase.")
    else:
        print("Create the datebase successful.")
    con = sqlite3.connect("Address.db")
    cur = con.cursor()
    x = AddressBook(con, cur)
    while True:
        Do = int(input("-----Please input what are want to do?(1.Select   2.Delete   3.Upgrade   4.Insert   0.Exit)：-----"))
        if Do == 0:
            break
        elif Do == 1:
            x.selectInfo()
        elif Do == 2:
            x.deleteInfo()
        elif Do == 3:
            x.updateInfo()
        elif Do == 4:
            x.insertInfo()
        else:
            print("-----The number inputed was wrong！-----")
    cur.close()
    con.close()

main()
