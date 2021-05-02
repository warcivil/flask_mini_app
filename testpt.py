from werkzeug.security import check_password_hash, generate_password_hash
from connect_bd_pattern import db_connect

@db_connect
def register_page(sql_connect=None, cursor=None):
        dUN = "1"
        try_auth_query = f"SELECT id, username, password FROM info_about_users WHERE username = '{dUN}' "
        rows = cursor.execute(try_auth_query)
        rows = rows.fetchall()
        for row in rows:
            print(row)
        if(len(rows) == 1):
            return "USER EXIST"
    
register_page()