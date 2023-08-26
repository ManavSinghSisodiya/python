import pymysql as sql
try:    
    conn=sql.connect(host='localhost',port=3306,user='root',passwd='00000',database='lenevo')
    smt=conn.cursor()
    q="SELECT * FROM lenevo.products;"
    smt.execute(q)
    records=smt.fetchall()
    print(records)
    conn.close()
    
except Exception as err:
    print("error:",err)    