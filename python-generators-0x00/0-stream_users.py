import mysql.connector
from mysql.connector import errorcode
from seed import connect_to_prodev

def stream_users():
    connection = connect_to_prodev()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_SYNTAX_ERROR:
            print("Syntax error" )
    finally:
        cursor.close()
        connection.close()


