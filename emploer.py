from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os


def employer_create_table():
    sql_connect = sqlite3.Connection(
        "/Users/sif/Desktop/flaskg/flaskstr/info.db")
    cursor = sql_connect.cursor()
    try_login_query = "SELECT id, name, surname, post FROM employer"
    rows = cursor.execute(try_login_query)
    rows = rows.fetchall()
    return render_template('home.html', content=rows)


def get_employer():
    return render_template('employerTable.html')


def read_bd():
    UN = request.form['username']
    SR = request.form['surname']
    PR = request.form['post']
    sql_connect = sqlite3.Connection(
        "/Users/sif/Desktop/flaskg/flaskstr/info.db")
    cursor = sql_connect.cursor()
    auth_query = f"INSERT INTO employer(name, surname, post) VALUES('{UN}','{SR}', '{PR}')"
    rows = cursor.execute(auth_query)
    sql_connect.commit()
    rows.close()
    return redirect(url_for('home'))


def update_bd(index):
    UN = request.form['username']
    SR = request.form['surname']
    PR = request.form['post']
    sql_connect = sqlite3.Connection(
        "/Users/sif/Desktop/flaskg/flaskstr/info.db")
    cursor = sql_connect.cursor()
    auth_query = f"UPDATE employer SET name='{UN}', surname='{SR}', post='{PR}' WHERE id='{int(index)+1}'"
    rows = cursor.execute(auth_query)
    sql_connect.commit()
    rows.close()
    return redirect(url_for('home'))
