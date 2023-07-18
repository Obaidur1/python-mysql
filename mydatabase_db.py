import mysql.connector

db = mysql.connector.connect(
    host="localhost", username="root", passwd="password", database="mydatabase"
)
