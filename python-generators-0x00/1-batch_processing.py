from seed import connect_to_prodev
from mysql.connector import errorcode
import mysql.connector

def stream_users_in_batches(batch_size):
    connection  = connect_to_prodev()
    if connection is None:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age']> 25:
                print(user)
batch_processing(2)