from mydatabase_db import db

mycursor = db.cursor()
sql_command = """
UPDATE student
SET first_name = "Nura"
WHERE roll = 12;
"""
mycursor.execute(sql_command)
db.commit()
