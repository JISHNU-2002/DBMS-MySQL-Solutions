import pymysql

# Establish the connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="DEMO"
)

# Create a cursor object
cursor = connection.cursor()

# Insert data into the table
name = str(input('Enter employee name : '))
department = str(input('Enter employee department : '))
salary = float(input('Enter employee salary : '))

# MySQL uses %s for all types of data, and PyMySQL handles the conversion internally
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", (name, department, salary))

# Commit the changes
connection.commit()  

# Retrieve and print data from the table
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()