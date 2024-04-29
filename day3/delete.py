import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user = "sunbeam",
    password ="sunbeam",
    database ="iotdb"
)
def delete_employe(empid):
    #conn = mysql.connector.get_connection()
    query= f"delete from emp_info where empid=%s;"
    #query= f"update from emply where emid=%s;"
    val=(empid,)
    
    cursor = conn.cursor()  
    cursor.execute(query,val)
    
    conn.commit()
    
    cursor.close()
    conn.close()
    
delete_employe(23)

