import mysql.connector
import os

connection = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_DATABASE']
)


cursor = connection.cursor()


with open('add_departments.sql', 'r') as file:
    sql_script = file.read()
    sql_commands = sql_script.split(';')
    
    for command in sql_commands:
        if command.strip():
            cursor.execute(command)

connection.commit() # Commit all changes at once
cursor.close()  # Close the cursor
connection.close()  # Close the connection

print('Database changes applied successfully!!!')
