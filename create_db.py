import mysql.connector


db = mysql.connector.connect(host="localhost", username="root", passwd="password")

mycursor = db.cursor()
db_name = "mydatabase"
sql_command = "CREATE DATABASE " + db_name
mycursor.execute(sql_command)
