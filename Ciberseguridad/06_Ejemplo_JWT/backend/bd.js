const mysql = require('mysql2');
require('dotenv').config();

// Crear una conexión con la base de datos
const db = mysql.createConnection({
    host: process.env.BD_HOST,
    user: process.env.BD_USER,
    password: process.env.BD_PASSWORD,
    database: process.env.BD_NAME
});

// Verificar conexión
db.connect(err => {
    if (err) {
        console.error("❌ Error al conectar a la base de datos:", err);
        process.exit(1); // Detiene el servidor si la conexión falla
    }

    console.log("✅ Conectado a la base de datos MySQL");
});

module.exports = db;
