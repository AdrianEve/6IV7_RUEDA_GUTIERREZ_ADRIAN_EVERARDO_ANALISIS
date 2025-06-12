const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs'); // corregido
const jwt = require('jsonwebtoken');
const db = require('../bd');

// Ruta de registro
router.post('/register', async (req, res) => {
    const { email, password } = req.body;

    try {
        const hashed = await bcrypt.hash(password, 10);

        db.query('INSERT INTO usuarios (email, password) VALUES (?, ?)', [email, hashed], (err, result) => {
            if (err) {
                console.log('Error al registrar al usuario:', err);
                return res.status(500).json({ message: 'Error al registrar' });
            }

            console.log("Usuario registrado con el ID", result.insertId);
            res.status(200).json({ message: 'Usuario registrado' });
        });
    } catch (error) {
        console.log('Error en el servidor al momento de registrar:', error);
        res.status(500).json({ message: 'Error interno del servidor' });
    }
});

// Ruta de login
router.post('/login', (req, res) => {
    const { email, password } = req.body;

    db.query('SELECT * FROM usuarios WHERE email = ?', [email], async (err, result) => {
        if (err) {
            console.log('Error en la consulta del login:', err);
            return res.status(500).json({ message: 'Error en el servidor' });
        }

        if (result.length === 0) {
            return res.status(401).json({ message: 'Credenciales inválidas' });
        }

        const user = result[0];

        const valid = await bcrypt.compare(password, user.password);
        if (!valid) {
            console.warn("Contraseña incorrecta para usuario:", email);
            return res.status(401).json({ message: 'Contraseña incorrecta' });
        }

        const token = jwt.sign(
            { id: user.id, email: user.email },
            process.env.JWT_SECRET,
            { expiresIn: '1h' }
        );

        console.log('Token generado para el usuario:', user.email);
        res.json({ token });
    });
});

module.exports = router;
