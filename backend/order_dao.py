from sqlconnection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()

    # Insert into 'orders' table
    order_query = "INSERT INTO orders(cust_name, total_cost, date) VALUES (%s, %s, %s)"
    order_data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(order_query, order_data)

    # Get the last inserted order_id
    order_id = cursor.lastrowid

    # Insert into 'orderdetail' table
    order_details_query = "INSERT INTO orderdetail(order_id,product_id, quantity, total) VALUES (%s,%s, %s, %s)"
    order_detail_data = []
    
    for order_detail_record in order['order_details']:
        order_detail_data.append((
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price']),
        ))

    cursor.executemany(order_details_query, order_detail_data)
    connection.commit()

    return order_id
def get_all_orders(connection):
    cursor=connection.cursor()
    query=("select * from orders")
    cursor.execute(query)
    response=[]
    for (order_id,cust_name,total_cost,date) in cursor:
        response.append({
            'datetime':date,
            'order_id':order_id,
            'customer_name':cust_name,
            'total':total_cost,
            
        })
    return response

if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_orders(connection))