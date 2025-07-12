import sqlite3
import functools
import logging


def log_queries(func):
    format = '%(levelname)s - %(asctime)s - %(message)s'
    logging.basicConfig(filename="query.log", filemode="a", format=format)
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' else (args[0] if args else '')
        try:
            func(*args, **kwargs)
        except sqlite3.Error as err:
            logger.error(f'{err} : {query}')
        except Exception as exp:
            logger.critical(f'{err} : {query}')

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