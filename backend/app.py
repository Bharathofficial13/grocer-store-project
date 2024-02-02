import json
from flask import Flask,request,jsonify
import product_dao 
import order_dao
from sqlconnection import get_sql_connection
from uom import get_uom as u;
from order_dao import insert_order
app=Flask(__name__)
connection=get_sql_connection()
@app.route('/getProducts',methods=['GET'])
def get_products():
      products= product_dao.get_all_products(connection)
      response=jsonify(products)
      response.headers.add('Access-Control-Allow-Origin','*')
      return response
@app.route('/insertProduct',methods=['POST'])
def insert_new_product():
      req = json.loads(request.form['data'])
      product_id=product_dao.insert_new_product(connection,req)
      response=jsonify({"product_id": product_id})
      response.headers.add('Access-Control-Allow-Origin','*')
      return response
@app.route('/deleteProduct',methods=['POST'])
def del_prod():
       return_id=product_dao.del_prod(connection,request.form['product_id'])
       response=jsonify({
              'product_id':return_id
       })
       response.headers.add('Access-Control-Allow-Origin','*')
       return response

@app.route('/getUOM',methods=['GET'])
def get_uom():
       response=u(connection)
       response=jsonify(response)
    
       response.headers.add('Access-Control-Allow-Origin','*')
       return response


@app.route('/insertOrder',methods=['POST'])
def insert_order():
      req = json.loads(request.form['data'])
      order_id=order_dao.insert_order(connection,req)
      response=jsonify({"order_id": order_id})
      response.headers.add('Access-Control-Allow-Origin','*')
      return response

@app.route('/getAllOrders',methods=['GET'])
def get_all_orders():
       response=order_dao.get_all_orders(connection)
       response=jsonify(response)
       response.headers.add('Access-Control-Allow-Origin','*')
       return response
if __name__ =="__main__":
        app.run(port=5000)