from flask import Flask, render_template, request, redirect
import sqlite3
import os
from emploer import  employer_create_table

auth = False


def check_login():
    UN = request.form['username']
    PW = request.form['password']
    sql_connect = sqlite3.Connection(
        "/Users/sif/Desktop/flaskg/flaskstr/info.db")
    cursor = sql_connect.cursor()
    try_login_query = f"SELECT username, password FROM info_about_users WHERE username = '{UN}' AND password = '{PW}'"

    rows = cursor.execute(try_login_query)
    rows = rows.fetchall()
    if len(rows) == 1:
        global auth
        auth = True
        return employer_create_table()
    else:
        return 'bad login or password'
