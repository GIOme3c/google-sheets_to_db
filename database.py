import psycopg2

from config import DB_SETTINGS


def get_connection():
    return psycopg2.connect(**DB_SETTINGS)


def select_rqst(rqst_str):
    with get_connection().cursor() as cursor:
        cursor.execute(rqst_str)
        return cursor.fetchall()


def check_page_token(page_token):
    curr_page_token = select_rqst("""
    select variable_value from local_variables 
    where variable_name = 'current_page_token'
    """)[0][0]

    return page_token == curr_page_token
        

def update_orders(orders_data, page_token):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
                update local_variables
                set variable_value = {page_token}
                where variable_name = 'current_page_token'
                """)
        
        cursor.execute("delete from orders")
        for row in orders_data[1:]:
            cursor.execute(f"""
                    insert into orders
                    (number, order_id, price_usd, delivery_date)
                    values
                    ({row[0]},{row[1]},{row[2]},{repr(row[3])})
                    """)
            
        connection.commit()


def update_usd_course(current_course):
    db_course = select_rqst("""
            select variable_value from local_variables 
            where variable_name = 'usd_to_rub'
            """)[0][0]
    
    if db_course != current_course:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                    update local_variables
                    set variable_value = {current_course}
                    where variable_name = 'usd_to_rub'
                    """)
            connection.commit()


def get_orders():
    raw_response = select_rqst("select * from orders")
    orders = []
    for row in raw_response:
        orders.append({
            "number":row[0],
            "order_id":row[1],
            "price_usd":row[2],
            "price_rub":row[3],
            "delivery_date":row[4],
        })
    return orders
