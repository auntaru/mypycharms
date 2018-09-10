# https://www.w3schools.com/python/python_mysql_select.asp
#
# https://dev.mysql.com/doc/employee/en/employees-installation.html
# A sample MySQL database with an integrated test suite, used to test your applications and database servers
#
#

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
