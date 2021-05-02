from flask import Flask, render_template, request, redirect, url_for
from connect_bd_pattern import sql_query, db_connect
import sqlite3
import os


@sql_query("SELECT id, name, surname, post FROM employer")
def employer_create_table(rows=None):
    return render_template('home.html', content=rows)


def get_employer():
    return render_template('employerTable.html')


@db_connect
def read_bd(sql_connect=None, cursor=None):
    UN = request.form['username']
    SR = request.form['surname']
    PR = request.form['post']
    auth_query = f"INSERT INTO employer(name, surname, post) VALUES('{UN}','{SR}', '{PR}')"
    cursor.execute(auth_query)
    return redirect(url_for('home'))


@db_connect
def update_bd(index, sql_connect=None, cursor=None):
    UN = request.form['username']
    SR = request.form['surname']
    PR = request.form['post']
    auth_query = f"UPDATE employer SET name='{UN}', surname='{SR}', post='{PR}' WHERE id='{int(index)+1}'"
    cursor.execute(auth_query)
    return redirect(url_for('home'))
