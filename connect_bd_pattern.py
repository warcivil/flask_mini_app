import sqlite3
import os
import xlwt

#частичное решение проблемы DRY(dont repeat yourself) при подключение к бд
def sql_query(query):
    def db_instance(func):
        def wrapper(*args):
            sql_connect = sqlite3.Connection(
            os.getcwd()+"/info.db")
            cursor = sql_connect.cursor()
            try_login_query = query
            rows = cursor.execute(try_login_query)
            rows = rows.fetchall()
            value = func(rows)
            sql_connect.close()
            return value
        return wrapper
    return db_instance


def db_connect(func):
    def wrapper(*args):
        sql_connect = sqlite3.Connection(
        os.getcwd()+"/info.db")
        cursor = sql_connect.cursor()
        value = func(*args, sql_connect, cursor)
        sql_connect.commit()
        sql_connect.close()
        return value
    return wrapper