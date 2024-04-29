import mysql.connector
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user = "sunbeam",
    password ="sunbeam",
    database ="iotdb"
)

conn=get_connection()
   # query = f"insert into emply values({emid},'{name}','{deparment}','{email}',{salary},{doj});"
query1=f"select *from emp_info;"

cursor = conn.cursor()
cursor.execute(query1)
records=cursor.fetchall()
#print(records)
for record in records:
    print(record) 
    #emidquery

conn.commit()
cursor.close()
conn.close() 

"""
conn=get_connection()
query2=f"select * from emply order by salary DESC LIMIT 1; "
cursor.execute(query2)
record1=cursor.fetchall()
print(record1)
conn.commit()
cursor.close()
conn.close() """
