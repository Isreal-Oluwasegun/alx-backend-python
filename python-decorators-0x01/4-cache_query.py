import time
import sqlite3 
import functools
from datetime import datetime


query_cache = {}

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

def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else '')
        if query in query_cache:
            return query_cache[query]
        try:
            result = func(*args, **kwargs)
            query_cache[query] = result
            return result
        except sqlite3.Error as err:
            print(f"error: {err}")
            return 
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")