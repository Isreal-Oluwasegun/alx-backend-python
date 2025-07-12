import sqlite3 
import functools
from datetime import datetime


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        date = datetime.now()
        try:
            result = func(conn, *args, **kwargs)
            return result
        except sqlite3.Error as err:
            print(f'{date} - {err} - {conn}')
        finally:
            conn.close()
            print("connection closed gracefully")
    return wrapper

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('sql') if 'sql' in kwargs else (args[0] if args else '')
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("done")
            return result
        except sqlite3.Error as err:
            print(f"Trasaction failed: {err}")
            conn.rollback()
    return wrapper   



@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    cursor.close()
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')