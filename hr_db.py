import mysql.connector

hr_db = mysql.connector.connect(
    host="localhost", username="root", passwd="password", database="hr"
)
