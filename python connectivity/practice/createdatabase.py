import pymysql as sql
conn=sql.connect(host='localhost',port=3306,user='root',passwd='00000')

smt=conn.cursor()
q="create database india"
smt.execute(q)
conn.comit()
conn.close()
