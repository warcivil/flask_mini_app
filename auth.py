from flask import Flask, request, make_response
import sqlite3
import os
from emploer import  employer_create_table
from connect_bd_pattern import db_connect
from werkzeug.security import check_password_hash
auth = False
@db_connect
def check_login(sql_connect=None, cursor=None):
    UN = request.form['username']
    PW = request.form['password']
    try_auth_query = f"SELECT username, password FROM info_about_users WHERE username = '{UN}' "

    rows = cursor.execute(try_auth_query)
    rows = rows.fetchall()
    for row in rows:
        if(check_password_hash(row[1], PW)):
            res = make_response("success")
            res.set_cookie("logged", "True")
            return employer_create_table()
    return 'bad login or password'
