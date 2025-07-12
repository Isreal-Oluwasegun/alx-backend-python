import time
import sqlite3 
import functools
from datetime import datetime

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else '')
        try:
            date = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
            result = func(conn, *args, **kwargs)
            return result
        except sqlite3.Error as err:
            print(f'{date} - {err} - {query}')
        finally:
            conn.close()
            print("connection closed succesfully")
    return wrapper


def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for retry in range(1, retries+1):
                try:
                    result = func(*args, **kwargs)
                    time.sleep(delay)
                    return result
                except Exception:
                    print("error")
        return wrapper
    return decorator
    
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)