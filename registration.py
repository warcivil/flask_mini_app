from flask import  Flask, render_template, request
import sqlite3
from emploer import  employer_create_table
from os import getcwd
from connect_bd_pattern import db_connect
from werkzeug.security import  generate_password_hash
@db_connect
def register_page(sql_connect=None, cursor=None):
    if request.method == 'POST':
        dUN = request.form['username']
        dPW =  generate_password_hash(request.form['password'])
        try_auth_query = f"SELECT username, password FROM info_about_users WHERE username = '{dUN}' AND password = '{dPW}'"
        rows = cursor.execute(try_auth_query)
        rows = rows.fetchall()
        if(len(rows) == 1):
            return "USER EXIST"
        else:
            auth_query = f"INSERT INTO info_about_users(username, password) VALUES('{dUN}','{dPW}')"
            rows = cursor.execute(auth_query)
            return employer_create_table()
    return render_template('reg.html')