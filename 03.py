#计算机172班  1520173186   赖炳铮

import xlrd
import xlsxwriter
import sqlite3
import json
import csv

def readCSV():
    in_cvs = csv.reader(open('out_csv.csv', 'r'))
    for i in in_cvs:
            print(i)

def writeCSV(ls):
    out_csv = open("out_csv.csv", "w", newline="")
    con = csv.writer(out_csv)
    con.writerow(ls[0])
    for i in ls[1:]:
        list = []
        for j in i:
            list.append(i[j])
        con.writerow(list)
    out_csv.close()

def readJSON():
    in_json = open("out_rk.json", "r", encoding="gbk")
    ls = json.load(in_json)
    data = list(ls[0].keys())
    for item in ls:
        data.append(list(item.values()))
    in_json.close()

def writeJSON(ls):
    out_json = open("out_rk.json", "w")
    for i in range(1, len(ls)):
        ls[i] = dict(zip(ls[0], ls[i]))
    json.dump(ls[1:], out_json, sort_keys = True, indent = 5, ensure_ascii = False)
    out_json.close()

def readEXCEL():
    in_wb = xlrd.open_workbook("rk_scores.xlsx")
    ws = in_wb.sheet_by_index(0)
    ls = []
    for i in range(ws.nrows):
        ls.append(ws.row_values(i))
    return ls

def writeEXCEL(ls):
    out_wb = xlsxwriter.Workbook("out_excel.xlsx")
    bold = out_wb.add_format({"bold" : True})
    color = out_wb.add_format({"color" : "red"})
    ws = out_wb.add_worksheet("sheet1")
    for i in range(len(ls)):
        if i == 0:
            ws.write_row("A" + str(i + 1), ls[i], bold)
        else:
            ws.write_row("A" + str(i + 1), ls[i], color)
    out_wb.close()

def readSQLite():
    con = sqlite3.connect("rk.db")
    cur = con.cursor()
    result = cur.execute("select * from rkTable")
    for row in result:
        print("{} {} {} {}".format(*row))
    cur.close()
    con.close()

def writeSQLite(ls):
    con = sqlite3.connect("rk.db")
    cur = con.cursor()
    droptable_sql = "drop table if exists rkTable"
    cur.execute(droptable_sql)

    cur.execute("""
                create table rkTable(
                    "name" text not null,
                    "idcard" text not null, 
                    "mor_sorce" text not null,
                    "aft_sorce1" text not null,
                    "aft_sorce2" text not null
                );
        """)
    for i in range(len(ls) - 1):
        sqlstr = "insert into rkTable(name, idcard, mor_sorce, aft_sorce1, aft_sorce2) values (?, ?, ?, ?, ?) "
        cur.execute(sqlstr, (ls[i + 1][0], ls[i + 1][1], ls[i + 1][2], ls[i + 1][3], ls[i + 1][4]))
    con.commit()
    cur.close()
    con.close()

def main():
    ls = readEXCEL()
    writeEXCEL(ls)

    writeSQLite(ls)
    readSQLite()

    writeJSON(ls)
    readJSON()

    writeCSV(ls)
    readCSV()

main()