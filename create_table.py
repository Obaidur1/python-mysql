import mysql.connector

db = mysql.connector.connect(
    host="localhost", username="root", passwd="password", database="mydatabase"
)

mycursor = db.cursor()

sql_command = """
CREATE TABLE student(
roll int,
first_name varchar(30),
last_name varchar(30)
);

"""
mycursor.execute(sql_command)
