import pymysql as sql
conn=sql.connect(host='localhost',port=3306,user='root',passwd='00000',database='india')

smt=conn.cursor()
q="create table places(placeid int   , placename varchar(20) ,city char(20) ,state char(40) , distance_from_capital int(1000),primary key(placeid))"
smt.execute(q)
conn.commit()
conn.close()