
Tecnologías Utilizadas
======================

Este proyecto ha sido desarrollado utilizando una variedad de tecnologías, frameworks y librerías que son fundamentales para su funcionamiento. A continuación, se detallan las herramientas principales utilizadas:

- **Django**: Un framework de desarrollo web de alto nivel para Python que fomenta el desarrollo rápido y el diseño limpio y pragmático.

- **Django REST Framework**: Un potente y flexible toolkit para construir APIs web, utilizado en este proyecto para desarrollar las interfaces de programación de aplicaciones (APIs) que permiten la interacción con el sistema de seguridad del ERP.

- **coreapi**: Utilizado para generar documentación interactiva de las APIs. Esto facilita la comprensión y el uso de las APIs proporcionadas por el sistema.

- **djangorestframework-simplejwt**: Una extensión para Django REST Framework que utiliza tokens JWT para autenticar a los usuarios. Cuando un usuario se loguea correctamente, el sistema genera un token que verifica y controla los permisos del usuario, permitiéndole acceder y operar dentro de las distintas APIs del ERP.

- **SQLite3**: Como sistema de gestión de bases de datos, SQLite3 ofrece una solución ligera y de configuración sencilla sin necesidad de un servidor de bases de datos separado, ideal para proyectos de tamaño mediano y para entornos de desarrollo.

Estas tecnologías han sido seleccionadas por su robustez, flexibilidad y compatibilidad con los estándares modernos de desarrollo web, asegurando que el sistema de seguridad del ERP sea tanto escalable como seguro.

Configuración de la Base de Datos
=================================

Para detalles sobre la configuración inicial de la base de datos, incluyendo los comandos SQL para poblar las tablas, consulta el archivo `explicacion_BD.rst`. Este archivo contiene instrucciones detalladas y los comandos necesarios para configurar correctamente la base de datos para el entorno de desarrollo.

Estructura del Proyecto
=======================

Directorio Principal
--------------------

- PRUEBASTONE1: Carpeta raíz del proyecto.

Subdirectorio ERP
-----------------

- ERP: Contiene el orquestador del proyecto.
  - settings.py: Archivo de configuraciones principales del proyecto.

Aplicaciones de Django
----------------------

- contabilidad: Gestiona las transacciones financieras.
- gestion_proyectos: Administra la gestión y administración de proyectos.
- inventario: Maneja los recursos materiales del negocio.
- rh: Controla la información relacionada con recursos humanos.
- security: Gestiona permisos, roles, y la autenticación de usuarios mediante tokens.

Archivos en el Nivel de las Apps
-------------------------------

- db.sqlite3: Archivo de base de datos SQLite que contiene todas las tablas y datos del proyecto.
- manage.py: Script de utilidad que permite interactuar con este proyecto Django desde la línea de comandos para realizar tareas como migraciones, pruebas, o arrancar el servidor de desarrollo.
- requirements.txt: Lista de todas las librerías de Python necesarias para ejecutar el proyecto, útil para configurar rápidamente el entorno de desarrollo.

Descripción de la estructura del proyecto
----------------------------------------

Dentro de la carpeta principal PRUEBASTONE1, se encuentra la carpeta ERP que actúa como el corazón del proyecto con el archivo settings.py para las configuraciones. Al mismo nivel, se encuentran diversas aplicaciones que son módulos esenciales del sistema, permitiendo a los usuarios realizar operaciones a través de API Rest. La app 'security' es crucial por gestionar la seguridad a nivel de permisos y autenticación mediante tokens, añadiendo una capa de seguridad y dinamismo al interactuar con las APIs. ...

Descripción del Proyecto
========================

Objetivo
--------

El proyecto está diseñado para abordar el problema de la accesibilidad según los roles y permisos asignados a cada usuario. El objetivo es limitar el acceso a diferentes módulos del sistema y permitir transacciones API REST.

Funcionalidades
---------------

- Transacciones API REST soportadas: GET, POST, PUT, PATCH, y DELETE.
- Validación de usuarios mediante credenciales (username, password).
- Generación de tokens mediante las mismas credenciales, permitiendo una interacción segura y controlada con el sistema.

Seguridad
---------

Implementamos una autenticación que limita el acceso y las acciones en el sistema basadas en los roles y permisos del usuario. Esta medida asegura que sólo los usuarios autorizados puedan acceder a la información y funcionalidades específicas.

Diseño del Modelo de Base de Datos para Gestión de Usuarios, Roles y Permisos
=============================================================================

1. Flexibilidad y Separación
----------------------------

- `Rol`: Define conjuntos de permisos agrupados que representan funciones específicas dentro de la aplicación.
- `Permiso`: Detalla acciones específicas permitidas, como crear o modificar recursos, permitiendo un control granular.

2. Asociación Flexible
----------------------

- `UsuarioRol`: Asocia usuarios con roles. Permite múltiples roles por usuario y viceversa, reflejando la diversidad de funciones de los usuarios.

3. Modelado Preciso y Extensible
-------------------------------

- Proporciona una base sólida para la seguridad y la gestión efectiva del acceso, con la posibilidad de extender y adaptar el sistema a necesidades futuras.

4. Buenas Prácticas y Normalización
-----------------------------------

- El diseño sigue buenas prácticas de normalización y asegura la integridad referencial, facilitando la mantenibilidad y la escalabilidad del sistema.

Endpoints del Proyecto
======================

Ejemplo Endpoint módulos ERP::

    http://127.0.0.1:8000/api/contabilidad/transacciones/
    http://127.0.0.1:8000/api/gestion_proyectos/proyectos/
    http://127.0.0.1:8000/api/inventario/inventario/
    http://127.0.0.1:8000/api/rh/transacciones/

Ejemplo Endpoint generar token por usuario::

    http://127.0.0.1:8000/api/token/

Ejemplo Endpoint documentación general APIs::

    http://127.0.0.1:8000/docs/
