# https://www.w3schools.com/python/python_mysql_select.asp

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="employees"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)