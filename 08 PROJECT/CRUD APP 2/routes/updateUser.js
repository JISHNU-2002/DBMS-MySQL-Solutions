const express = require('express');
const router = express.Router();
const db = require('../db');

router.put('/:id', (req, res) => {
  const id = req.params.id;
  const { name, email } = req.body;
  db.query('UPDATE users SET name = ?, email = ? WHERE id = ?', [name, email, id], (err, results) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.json({ id, name, email });
    // console.log('User Recored Update Successful')
  });
});

module.exports = router;
