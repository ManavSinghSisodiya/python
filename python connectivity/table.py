import pymysql as sql
try:    
    conn=sql.connect(host='localhost',port=3306,user='root',passwd='00000',database='lenevo')
    smt=conn.cursor()
    q="create table products(productid int primary key, name varchar(25),price decimal(10))"
    smt.execute(q)
    conn.commit()
    print('sucess')
    conn.close()
    
except Exception as err:
    print("error:",err)    