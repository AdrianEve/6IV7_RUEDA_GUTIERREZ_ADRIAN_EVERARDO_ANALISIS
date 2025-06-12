const express = require('express');
const cors = require('cors');
const authRouters = require('./routes/auth');
require('dotenv').config();

const app = express();

// Verificar que JWT_SECRET esté definido
if (!process.env.JWT_SECRET) {
    console.error('❌ Error: JWT_SECRET no definido en el archivo .env');
    process.exit(1);
}

// Middlewares
app.use(cors());
app.use(express.json());

// Rutas
app.use('/api/auth', authRouters);

// Servidor
app.listen(3000, () => {
    console.log('🚀 Servidor corriendo en http://localhost:3000');
});
