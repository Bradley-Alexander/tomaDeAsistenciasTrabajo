---
title: "Casos de Uso - Grupo 1"
format: html
---
## CU-001: Inicio de sesión
| Campo | Descripción |
|---|---|
| **Identificador** | CU-001 |
| **Nombre** | Inicio de sesión |
| **Descripción** | Permite que los usuarios accedan al sistema mediante correo y clave válidos, para concederles los permisos correspondientes. |
| **Actores** | Usuario (Administrador, Entrenador, Pasante, Atleta) |
| **Pre condiciones** | El usuario debe estar registrado en el sistema. |
| **Post Condiciones** | El usuario queda autenticado y accede a las funcionalidades del sistema según su rol. |
| **Referencia a requisitos** | RF-001 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa correo y contraseña en el formulario de login. | Valida formato de los datos. |
| 2 | Confirma el envío del formulario. | Verifica credenciales en la base de datos. |
| 3 | | Si son correctas, genera token de sesión y redirige al usuario. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa credenciales inválidas. | Muestra mensaje de "Credenciales incorrectas". |
| 2 | Deja campos vacíos. | Muestra mensaje de "Campos requeridos". |
**Errores:**
| # | Error |
|---|---|
| 1 | Error de conexión con el servidor. |
| 2 | Cuenta bloqueada o inactiva. |
---
## CU-002: Cambio de roles de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-002 |
| **Nombre** | Cambio de roles de usuarios |
| **Descripción** | El administrador del sistema podrá asignar, cambiar o remover roles a los usuarios registrados (entrenador, atleta, pasante). |
| **Actores** | Administrador |
| **Pre condiciones** | El administrador debe haber iniciado sesión y existir usuarios registrados. |
| **Post Condiciones** | El rol del usuario es actualizado en el sistema. |
| **Referencia a requisitos** | RF-002 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona la opción de gestión de usuarios. | Muestra el listado de usuarios. |
| 2 | Selecciona un usuario específico y la opción de editar rol. | Muestra el formulario con los roles disponibles. |
| 3 | Selecciona el nuevo rol (Entrenador, Atleta, Pasante) y guarda. | Valida la selección y actualiza el rol en base de datos. |
| 4 | | Muestra mensaje de "Rol actualizado con éxito". |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela la operación. | Retorna al listado sin cambios. |
| 2 | Intenta asignar un rol ya asignado. | Muestra mensaje informativo. |
**Errores:**
| # | Error |
|---|---|
| 1 | Fallo al conectar con la base de datos. |
| 2 | El usuario fue eliminado mientras se editaba. |
---
## CU-003: Registro de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-003 |
| **Nombre** | Registro de usuarios |
| **Descripción** | El sistema permitirá al administrador registrar nuevos usuarios ingresando sus datos personales y tipo de usuario. |
| **Actores** | Administrador |
| **Pre condiciones** | El administrador debe haber iniciado sesión. |
| **Post Condiciones** | Un nuevo usuario es creado en el sistema. |
| **Referencia a requisitos** | RF-003 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona la opción de "Nuevo Usuario". | Muestra el formulario de registro. |
| 2 | Ingresa identificación, nombres, apellidos, dirección, teléfono, correo y selecciona tipo. | Valida el formato de los datos en tiempo real. |
| 3 | Confirma el registro. | Verifica que el correo/identificación no existan. Crea el usuario. |
| 4 | | Muestra mensaje de "Usuario registrado exitosamente". |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa un correo ya registrado. | Muestra error "El correo ya está en uso". |
| 2 | Ingresa datos con formato inválido. | Marca los campos erróneos y bloquea el guardado. |
**Errores:**
| # | Error |
|---|---|
| 1 | Error interno del servidor al guardar. |
---
## CU-004: Modificación de datos de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-004 |
| **Nombre** | Modificación de datos de usuarios |
| **Descripción** | El sistema permitirá modificar los datos personales y tipo de usuario de una cuenta existente. |
| **Actores** | Administrador |
| **Pre condiciones** | El administrador debe haber iniciado sesión y el usuario a editar debe existir. |
| **Post Condiciones** | Los datos del usuario quedan actualizados. |
| **Referencia a requisitos** | RF-004 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Busca y selecciona al usuario a modificar. | Carga los datos actuales del usuario en el formulario. |
| 2 | Modifica los campos deseados (Nombres, Apellidos, Dirección, Teléfono, Tipo). | Valida los nuevos datos. |
| 3 | Guarda los cambios. | Actualiza el registro en la base de datos. |
| 4 | | Muestra confirmación de "Datos actualizados". |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Intenta dejar campos obligatorios vacíos. | Muestra alerta de validación. |
| 2 | No realiza cambios y sale. | No se afecta la base de datos. |
**Errores:**
| # | Error |
|---|---|
| 1 | Error de concurrencia (alguien más modificó el usuario). |
| 2 | Error de conexión. |
---
## CU-005: Listado de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-005 |
| **Nombre** | Listado de usuarios |
| **Descripción** | El sistema permitirá listar los datos de los usuarios con sus respectivos roles asignados. |
| **Actores** | Administrador |
| **Pre condiciones** | El administrador debe haber iniciado sesión. |
| **Post Condiciones** | Se visualiza la lista de usuarios registrados. |
| **Referencia a requisitos** | RF-005 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Accede al módulo de usuarios. | Consulta la base de datos de usuarios. |
| 2 | | Muestra una tabla/lista con Nombres, Apellidos, Correo, Rol, etc. |
| 3 | Utiliza filtros de búsqueda (opcional). | Filtra la lista según criterios. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No existen usuarios registrados. | Muestra mensaje "No hay usuarios registrados". |
**Errores:**
| # | Error |
|---|---|
| 1 | Fallo en la carga de datos. |
