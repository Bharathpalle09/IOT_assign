import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user = "sunbeam",
    password ="sunbeam",
    database ="iotdb"
)
emid = int(input("enter emid:"))
name =input("enter name")
deparment=input("enter deparment")
email=input("enter email")
salary=int(input("enter salary"))
doj=int(input("enter doj"))
query = f"insert into emp_info values({emid},'{name}','{deparment}','{email}',{salary},{doj});"
#delete =f"delete from emply where emid=%s;"
cursor = connection.cursor()
cursor.execute(query)
#emidquery
connection.commit()
cursor.close()
connection.close() 