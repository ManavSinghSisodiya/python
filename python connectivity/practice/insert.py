import pymysql as sql
conn=sql.connect(host='localhost',port=3306,user='root',passwd='00000',database='india')

smt=conn.cursor()
p_id=input('enter place id')
pname=input('enter place name')
city=input('enter city')
state=input('enter state')

q="insert into places values({1},{2},{3},{4})".format(p_id,pname,city,state)
smt.execute(q)
conn.commit()
conn.close()