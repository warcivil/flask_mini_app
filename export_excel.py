from flask import Flask, send_file
import sqlite3
import os
import xlwt


def export_excel():
    sql_connect = sqlite3.Connection(
        os.getcwd()+"/info.db")
    cursor = sql_connect.cursor()
    try_login_query = "SELECT id, name, surname, post FROM employer"
    rows = cursor.execute(try_login_query)
    rows = rows.fetchall()

    book = xlwt.Workbook()
    sheet1 = book.add_sheet("Sheet1")
    cols = ("id", "name", "surname", "post")
    
    row = sheet1.row(0)
    for i in range(len(cols)):
        row.write(i, cols[i])
    
    for num in rows:
        row = sheet1.row(num[0])
        for index in range(0, 4):
            row.write(index, num[index])
    
    book.save("export.xls")
    return send_file("export.xls")
