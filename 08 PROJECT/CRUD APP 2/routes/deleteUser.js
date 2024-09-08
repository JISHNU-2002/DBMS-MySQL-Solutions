const express = require('express');
const router = express.Router();
const db = require('../db');

router.delete('/:id', (req, res) => {
  const id = req.params.id;
  db.query('DELETE FROM users WHERE id = ?', [id], (err, results) => {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.status(204).send();
    // console.log('User Recored Delete Successful')
  });
});

module.exports = router;
