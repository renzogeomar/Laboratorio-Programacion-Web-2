-- Crear base de datos
CREATE DATABASE IF NOT EXISTS empresa_demo;
USE empresa_demo;

-- Crear tabla clientes
CREATE TABLE IF NOT EXISTS clientes (
  id_cliente VARCHAR(10) PRIMARY KEY,
  nombre_empresa VARCHAR(100),
  nombre_contacto VARCHAR(100),
  direccion VARCHAR(100),
  ciudad VARCHAR(50),
  codigo_postal VARCHAR(20),
  pais VARCHAR(50)
);

-- Insertar datos de prueba
INSERT INTO clientes (id_cliente, nombre_empresa, nombre_contacto, direccion, ciudad, codigo_postal, pais) VALUES
('ALFKI', 'Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany'),
('NORTS', 'North/South', 'Simon Crowther', 'South House 300 Queensbridge', 'London', 'SW7 1RZ', 'UK'),
('WOLZA', 'Wolski Zajazd', 'Zbyszek Piestrzeniewicz', 'ul. Filtrowa 68', 'Warszawa', '01-012', 'Poland');