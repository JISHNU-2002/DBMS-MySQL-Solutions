- Building a simple CRUD (Create, Read, Update, Delete) application with MySQL 
### Prerequisites
1. **MySQL**: Ensure MySQL is installed and running
2. **Python**: Install Python and pip
3. **Flask**: Install Flask using `pip install Flask`
4. **Flask-MySQLdb**: Install this package using `pip install Flask-MySQLdb`

### Step-by-Step Guide

#### 1. Set Up the MySQL Database

```sql
CREATE DATABASE CRUD_APP;
USE CRUD_APP;
```

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

#### 2. Create the Flask Application

Create a new directory for your project and inside that directory, create a file named `app.py`

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'DEMO'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    name = request.form['name']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM users WHERE id = %s', (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3. Create HTML Templates

Create a folder named `templates` in the same directory as `app.py`. Inside this folder, create a file named `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple CRUD App</title>
</head>
<body>
    <h1>Users</h1>
    <form action="/add" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Add User</button>
    </form>

    <ul>
        {% for user in users %}
        <li>
            {{ user[1] }} ({{ user[2] }})
            <form action="/update/{{ user[0] }}" method="POST" style="display:inline;">
                <input type="text" name="name" placeholder="Name" value="{{ user[1] }}" required>
                <input type="email" name="email" placeholder="Email" value="{{ user[2] }}" required>
                <button type="submit">Update</button>
            </form>
            <form action="/delete/{{ user[0] }}" method="POST" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### 4. Run the Application

Run the Flask application from your terminal:

```bash
python app.py
```

You should be able to access the application at `http://localhost:5000`. 


