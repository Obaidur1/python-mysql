import mysql.connector
from db import db

mycursor = db.cursor()
sql_command = """
INSERT INTO student
values(10,"Obaidur","Rahman"),(12,"Nur","Muhammad"); 
"""
mycursor.execute(sql_command)
db.commit()
