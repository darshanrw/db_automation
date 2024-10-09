# Full name: Darshan Wadekar 
# Student ID: 8934575 
# Class number: Fall Section 1 - Cloud DevOps
"""
import pymysql

# Create the database connection directly
connection = pymysql.connect(
    host='localhost',  
    user='root',  
    password='Secret55',  
    database='sampledb'
)



# Path to the SQL file
script_path = 'add_departments.sql'

# Read the SQL script from the file
with open(script_path, 'r') as file:
    sql_script = file.read()

# Create a cursor object to execute SQL queries
cursor = connection.cursor()  

# Execute each SQL statement individually (split by semicolon)
for statement in sql_script.split(';'):
    if statement.strip():  # Execute only non-empty statements
        cursor.execute(statement)

connection.commit()  # Commit all changes at once
cursor.close()  # Close the cursor
connection.close()  # Close the connection

print("Execution completed successfully")

"""

import mysql.connector
import os

connection = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_DATABASE']
)




# Ensure the SQL file name is in quotes
sql_file = 'add_departments.sql'  # The file name should be a string

# Open the SQL file and read its contents
with open(sql_file, 'r') as file:
    sql_script = file.read()

# Execute the SQL script
cursor = connection.cursor()

for command in sql_script.split(';'):
    if command.strip():
        cursor.execute(command)

connection.commit() # Commit all changes at once
cursor.close()  # Close the cursor
connection.close()  # Close the connection

print('Database changes applied successfully!')