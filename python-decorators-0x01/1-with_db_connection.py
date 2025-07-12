import sqlite3 
import functools
from datetime import datetime

def with_db_connection(func):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' else (args[0] if args else '')
        try:
            date = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
            result = func(conn, *args, **kwargs)
            return result
        except sqlite3.Error as err:
            print(f'{date} - {err} - {query}')
        finally:
            cursor.close()
            conn.close()
            print("connection closed succesfully")
            return None
        
    return wrapper

        
    

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)