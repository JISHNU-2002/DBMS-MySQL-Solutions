from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'CRUD_APP'

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
