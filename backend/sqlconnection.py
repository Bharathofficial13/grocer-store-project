import mysql.connector


__cnx=None
def get_sql_connection():
    global __cnx
    if __cnx == None:
          __cnx=mysql.connector.connect(user='root', password='bharath@2002',
          host='127.0.0.1',database='gs')
    return __cnx