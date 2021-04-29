from flask import  Flask, render_template, request
import sqlite3

def register_page():
    if request.method == 'POST':
        dUN = request.form['username']
        dPW = request.form['password']
        sql_connect = sqlite3.Connection("/Users/sif/Desktop/flaskg/flaskstr/info.db")
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
            return render_template('auth.html')
    return render_template('reg.html')