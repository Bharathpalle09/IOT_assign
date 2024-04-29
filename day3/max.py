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
query1=f"select * from emp_info order by salary DESC LIMIT 1 ;"
#query2=f"select * from emply order by salary DESC LIMIT 1 ;"

cursor = conn.cursor()
cursor.execute(query1)
records=cursor.fetchall()
#print(records)
#for record in records:
print(records) 
    #emidquery

conn.commit()
cursor.close()
conn.close() 
