# Import library
import mysql.connector as mydbconnection
from mysql.connector import Error


def connect():
    conn = None

    try:
        # Establish connection
        conn = mydbconnection.connect( host="127.0.0.1",
    port=3306,
    database="classicmodels",
    user="root",
    password="Perscholas2026$")
        
        # Perform SQL Operations
        # Return Results (get results from sql)
        if conn.is_connected():
            print('✅ Connected to MySQL DB')
    
    except Error as e:
        print(f'❌ Error: {e}')

    finally: # runs whether operation failed or not (Always runs)
        # Close our connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 DB Connection Closed')






# Module if state
if __name__ == '__main__':
    connect()