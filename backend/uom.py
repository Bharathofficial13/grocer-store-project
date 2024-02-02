def get_uom(connection):
    cursor=connection.cursor()
    query="Select * from uom"
    cursor.execute(query)
    response=[]
    for unit_id,unit in cursor:
        response.append({
            'uom_id':unit_id,
            'uom_name':unit
        })
    return response

if __name__=='__main__':
    from sqlconnection import get_sql_connection
    connection=get_sql_connection()
    print(get_uom(connection))