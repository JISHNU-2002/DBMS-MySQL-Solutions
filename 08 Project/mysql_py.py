import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="DEMO"
)

# Create a cursor object
cursor = conn.cursor()

# Insert data into the table
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", ('John Doe', 'HR', 55000))
conn.commit()  # Commit the changes

# Retrieve and print data from the table
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
