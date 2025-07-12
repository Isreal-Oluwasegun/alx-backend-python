import sqlite3
import functools
from datetime import datetime


def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        date =datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = kwargs.get('query') if 'query' else (args[0] if args else '')
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as err:
            print(f'{date} - {err} - {query}')
        except Exception as exc:
            print(f'{date} - {exc} - {query}')
        return func
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")