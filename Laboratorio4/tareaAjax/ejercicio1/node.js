const path = require('path');
const express = require('express');
const app = express();

// Servir archivos estáticos desde el directorio actual
app.use(express.static(__dirname));

app.listen(3000, () => {
    console.log('Servidor escuchando en http://localhost:3000');
});

