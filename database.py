import psycopg2

from config import DB_SETTINGS

def get_connection():
    return psycopg2.connect(**DB_SETTINGS)

def select_from_db(cursor, rqst):
    cursor.execute(rqst)
    return cursor.fetchall()



def get_orders():
    connection = get_connection()
    cursor = connection.cursor()
    
    select_orders_rqst = f"""
    select 
    """




def set_orders():
    pass