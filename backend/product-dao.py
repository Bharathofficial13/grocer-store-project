from sqlconnection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    # Fix: Use a string for the query
    query = "SELECT products.prod_id, products.prod_name, products.unit_id, products.price, uom.unit FROM products INNER JOIN uom ON products.unit_id = uom.unit_id ORDER BY prod_id;"
    
    cursor.execute(query)
    response = []

    for (prod_id, prod_name, unit_id, price, unit) in cursor:
        response.append({
            'product_id': prod_id,
            'name': prod_name,
            'unit_id': unit_id,
            'price_per_unit': price,
            'Unit': unit
        })


    return response
def insert_new_product(connection,product):
    
    cursor=connection.cursor()
    query=("Insert into products(prod_name,unit_id,price) values(%s,%s,%s)")
    data=(product['name'],product['unit_id'],product['price'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid
def del_prod(connection,prod_id):
    cursor=connection.cursor()
    query=("Delete from products where prod_id="+str(prod_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(del_prod(connection,8))
