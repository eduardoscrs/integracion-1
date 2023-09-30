const express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000;

// Configura la conexión a la base de datos MySQL
const db = mysql.createConnection({
  host: 'localhost',
  user: 'tu_usuario',
  password: 'tu_contraseña',
  database: 'tu_base_de_datos',
});

db.connect((err) => {
  if (err) {
    console.error('Error de conexión a la base de datos:', err);
  } else {
    console.log('Conexión exitosa a la base de datos');
  }
});

// Define tus rutas y controladores aquí

app.listen(port, () => {
  console.log(`Servidor escuchando en el puerto ${port}`);
});

app.get('/datos', (req, res) => {
    db.query('SELECT * FROM tabla_datos', (err, results) => {
      if (err) {
        console.error('Error en la consulta SQL:', err);
        res.status(500).json({ error: 'Error en la base de datos' });
      } else {
        res.json(results);
      }
    });
  });
  