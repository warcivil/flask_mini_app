from flask import  Flask, render_template, request, redirect, url_for
import sqlite3
from emploer import  employer_create_table
from os import getcwd

def register_page():
    if request.method == 'POST':
        dUN = request.form['username']
        dPW = request.form['password']
        sql_connect = sqlite3.Connection(getcwd()+"/info.db")
        cursor = sql_connect.cursor()
        try_auth_query = f"SELECT username, password FROM info_about_users WHERE username = '{dUN}' AND password = '{dPW}'"
        rows = cursor.execute(try_auth_query)
        rows = rows.fetchall()
        if(len(rows) == 1):
            return "USER EXIST"
        else:
            auth_query = f"INSERT INTO info_about_users(username, password) VALUES('{dUN}','{dPW}')"
            rows = cursor.execute(auth_query)
            sql_connect.commit()
            return employer_create_table()
    return render_template('reg.html')