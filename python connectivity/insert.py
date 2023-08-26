import pymysql as sql
try:    
    conn=sql.connect(host='localhost',port=3306,user='root',passwd='00000',database='lenevo')
    smt=conn.cursor()
    pid=input('enter product id:')
    pn=input('enter product name')
    rs=input('enter product price')
    
    q="insert into products values({0},'{1}',{2})".format(pid,pn,rs)
    print(q)
    smt.execute(q)
    conn.commit()
    conn.close()
    
except Exception as err:
    print("error:",err)  