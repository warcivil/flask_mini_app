from flask import Flask, request
import sqlite3
import os
from emploer import  employer_create_table
from connect_bd_pattern import db_connect
auth = False

@db_connect
def check_login(sql_connect=None, cursor=None):
    UN = request.form['username']
    PW = request.form['password']
    try_login_query = f"SELECT username, password FROM info_about_users WHERE username = '{UN}' AND password = '{PW}'"

    rows = cursor.execute(try_login_query)
    rows = rows.fetchall()
    if len(rows) == 1:
        global auth
        auth = True
        return employer_create_table()
    else:
        return 'bad login or password'
