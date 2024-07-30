
Info BD
=======

Para que el proyecto sea fácil de configurar y comenzar a probar, se utilizó SQLite3 como base de datos, que ya está configurada en el proyecto. En caso de errores, se adjuntan los comandos SQL para insertar datos en cada tabla. Para los usuarios, es necesario crearlos desde el panel de admin de Django usando un superusuario.

Para crear un superusuario en Django, ejecuta el siguiente comando en tu terminal::

    python manage.py createsuperuser

Sigue las instrucciones en pantalla para completar la creación del superusuario, que te permitirá acceder al panel de administración y gestionar los usuarios.

Los siguientes son los comandos SQL para insertar datos en las tablas del sistema:

Insertar datos en la tabla security_permiso::

    INSERT INTO security_permiso (id, nombre, descripcion) VALUES (1, 'Crear', 'Permite crear registros');
    INSERT INTO security_permiso (id, nombre, descripcion) VALUES (2, 'Leer', 'Permite leer registros');
    INSERT INTO security_permiso (id, nombre, descripcion) VALUES (3, 'Actualizar', 'Permite actualizar registros');
    INSERT INTO security_permiso (id, nombre, descripcion) VALUES (4, 'Eliminar', 'Permite eliminar registros');

Insertar datos en la tabla security_rol::

    INSERT INTO security_rol (id, nombre) VALUES (1, 'Administrador');
    INSERT INTO security_rol (id, nombre) VALUES (2, 'Gerente');
    INSERT INTO security_rol (id, nombre) VALUES (3, 'Empleado');
    INSERT INTO security_rol (id, nombre) VALUES (4, 'Recursos Humanos');
    INSERT INTO security_rol (id, nombre) VALUES (5, 'Contador');

Insertar datos en la tabla contabilidad_transaccion::

    INSERT INTO contabilidad_transaccion (descripcion, monto, fecha, es_ingreso) VALUES 
    ('Venta de producto', 1500.00, '2023-07-28', 1),
    ('Compra de material', 800.00, '2023-07-27', 0),
    ('Servicio de consultoría', 1200.00, '2023-07-26', 1),
    ('Pago de renta', 500.00, '2023-07-25', 0),
    ('Venta de licencias', 3000.00, '2023-07-24', 1);

Insertar datos en la tabla gestion_proyectos_proyecto::

    INSERT INTO gestion_proyectos_proyecto (nombre, descripcion, fecha_inicio, fecha_fin, presupuesto) VALUES 
    ('Desarrollo de ERP', 'Proyecto para el desarrollo de un sistema ERP.', '2023-01-01', '2023-12-31', 200000.00),
    ('Marketing Digital', 'Campaña de marketing para el tercer cuatrimestre.', '2023-06-01', '2023-12-31', 50000.00),
    ('Expansión de red', 'Proyecto de expansión de infraestructura de red.', '2023-05-01', NULL, 75000.00),
    ('Optimización logística', 'Proyecto para mejorar la logística interna.', '2023-04-01', '2023-10-01', 60000.00),
    ('Capacitación de personal', 'Programa de capacitación para empleados.', '2023-03-01', NULL, 30000.00);

Insertar datos en la tabla inventario_articulo::

    INSERT INTO inventario_articulo (nombre, cantidad, precio_unitario, descripcion) VALUES 
    ('Teclado Mecánico', 50, 120.00, 'Teclado mecánico retroiluminado'),
    ('Monitor LED 24"', 30, 180.00, 'Monitor LED de 24 pulgadas'),
    ('Mouse Inalámbrico', 100, 25.00, 'Mouse inalámbrico ergonómico'),
    ('Impresora Láser', 20, 300.00, 'Impresora láser color con WiFi'),
    ('Silla Ergonómica', 40, 150.00, 'Silla ergonómica ajustable');

Insertar datos en la tabla rh_empleado::

    INSERT INTO rh_empleado (nombre, apellido, email, fecha_contratacion, salario) VALUES 
    ('Juan', 'Pérez', 'juan.perez@email.com', '2022-01-15', 2500.00),
    ('María', 'González', 'maria.gonzalez@email.com', '2022-03-01', 2700.00),
    ('Carlos', 'Martínez', 'carlos.martinez@email.com', '2022-05-20', 3000.00),
    ('Luisa', 'Fernández', 'luisa.fernandez@email.com', '2022-07-07', 2800.00),
    ('Sofía', 'Rodríguez', 'sofia.rodriguez@email.com', '2022-09-15', 3200.00);

Los usuarios con sus roles y permisos son::

    5|Deibyt|Administrador|Actualizar
    5|Deibyt|Administrador|Crear
    5|Deibyt|Administrador|Eliminar
    5|Deibyt|Administrador|Leer
    4|Jose|Gerente|Actualizar
    4|Jose|Gerente|Crear
    4|Jose|Gerente|Eliminar
    4|Jose|Gerente|Leer
    7|Lorena|Recursos Humanos|Actualizar
    7|Lorena|Recursos Humanos|Crear
    7|Lorena|Recursos Humanos|Eliminar
    7|Lorena|Recursos Humanos|Leer
    6|Luis|Empleado|Actualizar
    6|Luis|Empleado|Crear
    6|Luis|Empleado|Leer
    3|Sandra|Contador|Leer
    2|Sebastian|Contador|Actualizar
    2|Sebastian|Contador|Crear
    2|Sebastian|Contador|Eliminar
    2|Sebastian|Contador|Leer

Si se desea modificar o añadir usuarios se tiene que hacer desde el panel administrativo de Django.
