from mysql.connector import errorcode
import mysql.connector
from seed import connect_to_prodev

def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor =  connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return None
    

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

for a in lazy_paginate(1):
    print(a)