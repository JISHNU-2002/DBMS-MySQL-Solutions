### 1. **Set Up Your Project**

1. **Create a new directory for your project:**

   ```bash
   mkdir express-mysql-crud
   cd express-mysql-crud
   ```

2. **Initialize a new Node.js project:**

   ```bash
   npm init -y
   ```

3. **Install the required packages:**

   ```bash
   npm install express mysql2 body-parser
   ```

### 2. **Set Up Your MySQL Database**

1. **Create a MySQL database and table:**

   Connect to your MySQL server and run:

   ```sql
   CREATE DATABASE mydatabase;

   USE mydatabase;

   CREATE TABLE users (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(100) NOT NULL UNIQUE
   );
   ```

### 3. **Create Your Express.js Application**

1. **Create a file named `app.js` in your project directory:**

   ```javascript
   const express = require('express');
   const mysql = require('mysql2');
   const bodyParser = require('body-parser');

   const app = express();
   const port = 3000;

   // Create MySQL connection
   const db = mysql.createConnection({
     host: 'localhost',
     user: 'root',
     password: 'mysql',
     database: 'DEMO'
   });

   db.connect((err) => {
     if (err) {
       console.error('Error connecting to MySQL:', err);
       return;
     }
     console.log('Connected to MySQL');
   });

   // Middleware
   app.use(bodyParser.json());
   app.use(bodyParser.urlencoded({ extended: true }));

   // Routes

   // Read all users
   app.get('/users', (req, res) => {
     db.query('SELECT * FROM users', (err, results) => {
       if (err) {
         return res.status(500).json({ error: err.message });
       }
       res.json(results);
     });
   });

   // Create a new user
   app.post('/users', (req, res) => {
     const { name, email } = req.body;
     db.query('INSERT INTO users (name, email) VALUES (?, ?)', [name, email], (err, results) => {
       if (err) {
         return res.status(500).json({ error: err.message });
       }
       res.status(201).json({ id: results.insertId, name, email });
     });
   });

   // Update a user
   app.put('/users/:id', (req, res) => {
     const id = req.params.id;
     const { name, email } = req.body;
     db.query('UPDATE users SET name = ?, email = ? WHERE id = ?', [name, email, id], (err, results) => {
       if (err) {
         return res.status(500).json({ error: err.message });
       }
       res.json({ id, name, email });
     });
   });

   // Delete a user
   app.delete('/users/:id', (req, res) => {
     const id = req.params.id;
     db.query('DELETE FROM users WHERE id = ?', [id], (err, results) => {
       if (err) {
         return res.status(500).json({ error: err.message });
       }
       res.status(204).send();
     });
   });

   // Start the server
   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}/`);
   });
   ```

### 4. **Run Your Application**

1. **Start the server:**

   ```bash
   node app.js
   ```

2. **Test Your Endpoints**

   You can use tools like [Postman](https://www.postman.com/) or `curl` to test the CRUD operations.

   - **Read all users:**

     ```bash
     curl http://localhost:3000/users
     ```

   - **Create a new user:**

     ```bash
     curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
     ```

   - **Update a user:**

     ```bash
     curl -X PUT http://localhost:3000/users/1 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
     ```

   - **Delete a user:**

     ```bash
     curl -X DELETE http://localhost:3000/users/1
     ```
