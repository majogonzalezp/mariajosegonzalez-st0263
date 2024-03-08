const express = require('express');
const readline = require('readline');
const app = express();
const puerto = 3000;

app.use(express.json());

// Endpoint para seleccionar archivos
app.post('/elegir_archivos', (req, res) => {
    const archivos = req.body.archivos;
    const indicesSeleccionados = req.body.indicesSeleccionados;

    const archivosElegidos = indicesSeleccionados.map(indice => parseInt(indice, 10) - 1)
                                                .filter(indice => indice >= 0 && indice < archivos.length)
                                                .map(indice => archivos[indice]);

    console.log("Archivos elegidos:", archivosElegidos);

    res.json({ archivosElegidos });
});

app.listen(puerto, () => {
    console.log(`Manejador de archivos en el puerto ${puerto}`);
});

