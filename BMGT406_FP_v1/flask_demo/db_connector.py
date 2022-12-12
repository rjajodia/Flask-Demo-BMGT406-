import mysql.connector

def get_connection():
    sql_conn = mysql.connector.connect(user='bmgt406_demo03', password='bmgt406_demo03', host='bmgt406.rhsmith.umd.edu', database='bmgt406_demo03_db')
    cursor = sql_conn.cursor()
    return cursor


def get_metadata(cursor, table_name):
    return execute_query(cursor, f"SELECT COLUMN_NAME, columnproperty(object_id('{table_name}'), \
        COLUMN_NAME ,'IsIdentity') AS IDENTITY_SPECIFICATION, * \
        FROM INFORMATION_SCHEMA.COLUMNS \
        WHERE TABLE_NAME = '{table_name}' AND TABLE_SCHEMA='dbo' ORDER BY ORDINAL_POSITION ASC")


def fetch_all(cursor, table_name):
    return execute_query(cursor, f"SELECT * FROM {table_name}")


def execute_query(cursor, sql, params=''):
    if params == '':
        cursor.execute(sql)
    else:
        cursor.execute(sql, params)
    results = cursor.fetchall()
    return results


def update_query(cursor, sql):
    #try:
    cursor.execute(sql)
    cursor.commit()
    success = True
    #except:
    #    success = False
    return success