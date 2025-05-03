<?php
// Conexión a la base de datos
$mysqli = new mysqli("localhost", "root", "", "empresa_demo");
if ($mysqli->connect_error) {
    exit('No se pudo conectar a la base de datos.');
}

// Consulta SQL ajustada a tu tabla "clientes"
$sql = "SELECT id_cliente, nombre_empresa, nombre_contacto, direccion, ciudad, codigo_postal, pais
        FROM clientes WHERE id_cliente = ?";

// Preparar y ejecutar
$stmt = $mysqli->prepare($sql);
$stmt->bind_param("s", $_GET['q']);
$stmt->execute();
$stmt->store_result();
$stmt->bind_result($id, $empresa, $contacto, $direccion, $ciudad, $postal, $pais);
$stmt->fetch();
$stmt->close();

// Mostrar resultados en tabla HTML
if ($id) {
    echo "<table border='1'>";
    echo "<tr><th>ID</th><td>$id</td></tr>";
    echo "<tr><th>Empresa</th><td>$empresa</td></tr>";
    echo "<tr><th>Contacto</th><td>$contacto</td></tr>";
    echo "<tr><th>Dirección</th><td>$direccion</td></tr>";
    echo "<tr><th>Ciudad</th><td>$ciudad</td></tr>";
    echo "<tr><th>Código Postal</th><td>$postal</td></tr>";
    echo "<tr><th>País</th><td>$pais</td></tr>";
    echo "</table>";
} else {
    echo "Cliente no encontrado.";
}
?>