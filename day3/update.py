import mysql.connector
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user = "sunbeam",
    password ="sunbeam",
    database ="iotdb"
)
def update_employe(salary,empid):
    conn=get_connection()
    query1=f"update emp_info SET salary=%s where empid=%s;"
    val=(empid,salary)
    cursor=conn.cursor()
    cursor.execute(query1,val)
    conn.commit()
    cursor.close()
    conn.close()
#emid=int(input("enter the emid"))

#salary=int(input("enter the salary"))

update_employe(42,50000) 
update_employe(23,30000)   