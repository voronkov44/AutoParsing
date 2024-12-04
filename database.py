import mysql.connector

# Конфигурация базы данных
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

def connect_db():
    return mysql.connector.connect(**db_config)

def close_db(connection):
    connection.close()

def execute_query(query, params=None):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    cursor.close()
    close_db(connection)

def fetch_all(query):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    close_db(connection)
    return results
