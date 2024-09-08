const express = require('express');
const bodyParser = require('body-parser');

const getUsersRouter = require('./routes/getUsers');
const createUserRouter = require('./routes/createUser');
const updateUserRouter = require('./routes/updateUser');
const deleteUserRouter = require('./routes/deleteUser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/', getUsersRouter);
app.use('/users', createUserRouter);
app.use('/users', updateUserRouter);
app.use('/users', deleteUserRouter);

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
