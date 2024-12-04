import pymysql
__cnx=None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = pymysql.connect(
          host="localhost",
          user="harshith",
          password="Password@123",
          database="grocery_store")
    return __cnx

