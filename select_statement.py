from hr_db import hr_db

mycr = hr_db.cursor()
sql_command = """
SELECT * 
FROM employees
WHERE salary > 2000
limit 10;
"""

mycr.execute(sql_command)
data = mycr.fetchall()
for i in data:
    print(i)
