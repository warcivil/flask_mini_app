from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os
import xlwt

def create_db(query):
    def db_instance(func):
        def wrapper(*args, **kwargs):
            sql_connect = sqlite3.Connection(
            os.getcwd()+"/info.db")
            cursor = sql_connect.cursor()
            try_login_query = query
            rows = cursor.execute(try_login_query)
            rows = rows.fetchall()
            return func(rows)
        return wrapper
    return db_instance
    
@create_db("SELECT id, name, surname, post FROM employer")
def export_excel(rows = None):
    book = xlwt.Workbook()

    # Add a sheet to the workbook
    sheet1 = book.add_sheet("Sheet1")

    # The data
    cols = ("id", "a", "surname", "post")

    row = sheet1.row(0)
    for i in range(len(cols)):
        row.write(i, cols[i])

    for num in rows:
        row = sheet1.row(num[0])
        for index in range(0, 4):
            row.write(index, num[index])
    book.save("test.xls")
    return 1


print(export_excel())
