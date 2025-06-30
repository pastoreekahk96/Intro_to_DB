import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user/password if necessary)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='W1zd0mk1&G1996'  # Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()

