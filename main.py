from flask import Flask, request, render_template, make_response, redirect, url_for
import sqlite3
import os
from registration import register_page
import  auth
from emploer import employer_create_table, get_employer, read_bd, update_bd
current_loc = os.path.dirname(os.path.abspath(__file__))
myapp = Flask(__name__)


@myapp.route("/")
def homepage():
    return render_template('auth.html')

@myapp.route('/home', methods=['GET', 'POST'])
def home():
    if(not auth.auth):
        return redirect(url_for('register_page_app'))
    return employer_create_table()


@myapp.route("/", methods=['POST'])
def check_login_app():
    return auth.check_login()


@myapp.route("/signup", methods=['GET', 'POST'])
def register_page_app():
    return register_page()

@myapp.route('/home/database_read/', methods=['POST', 'GET'])
def employer_write_bd():
    if request.method == 'GET':
        return get_employer()
    elif request.method == 'POST':
        return read_bd()

@myapp.route('/home/database_write/<index>/', methods=['POST', 'GET'])
def employer_update_bd(index):
    if(request.method == 'GET'):
        return render_template('update_bd_index.html')
    else:
        return update_bd(index)
if __name__ == "__main__":
    myapp.run()