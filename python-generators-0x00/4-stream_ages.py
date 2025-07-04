from seed import connect_to_prodev
import mysql.connector
from mysql.connector import errorcode
from functools import reduce

def stream_user_ages():
    connection = connect_to_prodev()
    if connection is None:
        return
    cursor =  connection.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM user_data") 
    for data in cursor:
        if not data:
            break
        yield data['age']

def average_age():
    sum_age = 0
    average_age = 0
    count = 0 
    for age in stream_user_ages():
        sum_age += age
        count +=1
    average_age = sum_age/count 
    print(f"Average age of users: {average_age}")

average_age()
    
