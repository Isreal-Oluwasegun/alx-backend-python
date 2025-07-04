import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

host = 'localhost'
user = 'root'
database = 'ALX_prodev'
password = 'Makinde0604'

def connect_db():
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password
            )
        print("Connection to database successfull")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(
            """CREATE DATABASE IF NOT EXISTS ALX_prodev """
        )
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database {database} already exist")
        else:
            print("Error", err)
    finally:
        cursor.close()
        connection.close()

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
            )
        print(f"Connection to {database} successfull")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    if connection is None:
        return
    else:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS user_data (
                            user_id CHAR(36) PRIMARY KEY,
                                name VARCHAR(255) NOT NULL,
                                email VARCHAR(255) NOT NULL,
                            age DECIMAL(3,0) NOT NULL)
                        """)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already exist")
            else:
                print("Error", err)


def insert_data(connection, filename):
    if connection is None:
        return
    
    cursor = connection.cursor()
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (
                row.get('user_id') or str(uuid.uuid4()),
                row['name'],
                row['email'],
                int(row['age'])
            ))
    connection.commit()
    cursor.close()
    print(f"Data from '{filename}' inserted successfully")

