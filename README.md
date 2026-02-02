---
title: "Casos de Uso - Grupo 1 (Detallado)"
format: html
---
## CU-001: Inicio de sesión
| Campo | Descripción |
|---|---|
| **Identificador** | CU-001 |
| **Nombre** | Inicio de sesión |
| **Descripción** | Permite a los usuarios autenticarse para acceder al dashboard correspondiente a su rol. |
| **Actores** | Usuario (Administrador, Entrenador, Pasante, Atleta) |
| **Pre condiciones** | El usuario debe estar registrado. |
| **Post Condiciones** | Redirección al Dashboard (`/dashboard`) y generación de token de sesión. |
| **Referencia a requisitos** | RF-001 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa correo y contraseña y pulsa "Iniciar Sesión". | Valida formato de correo y que la contraseña no esté vacía. |
| 2 | | Envía credenciales al servicio de autenticación (`authService.login`). |
| 3 | | Muestra notificación tipo Toast: "Inicio de sesión exitoso". |
| 4 | | Redirige automáticamente a la ruta `/dashboard`. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Usuario tiene 2FA activado. | Backend devuelve `temp_token`. Sistema muestra modal `TwoFactorLoginModal`. |
| 1.1 | Ingresa código 2FA. | Muestra Toast: "Verificación de 2 pasos completa" y redirige. |
| 2 | Usuario está en estado "Inactivo". | Error 403/401 específico. Sistema abre modal `VerificationModal` para reenviar correo. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Email formato inválido (sin @). | Validación HTML5 nativa o mensaje de error visual en campo. |
| 2 | Credenciales incorrectas. | Muestra Toast Error: "Error al iniciar sesión. Por favor verifica tus credenciales". |
| 3 | Usuario inactivo. | Muestra modal de verificación de cuenta. |
| 4 | Error de servidor. | Muestra Toast Error: Detalle del error o "Error desconocido". |
---
## CU-002: Cambio de roles de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-002 |
| **Nombre** | Cambio de roles de usuarios |
| **Descripción** | Permite al administrador modificar el rol de un usuario existente (ADMINISTRADOR, ENTRENADOR, ATLETA, REPRESENTANTE). |
| **Actores** | Administrador |
| **Pre condiciones** | Usuario debe existir en la lista. |
| **Post Condiciones** | El rol del usuario se actualiza en base de datos y en la interfaz. |
| **Referencia a requisitos** | RF-002 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | En la tabla de usuarios, pulsa botón "Cambiar Rol". | Muestra alerta modal (SweetAlert) con selector de roles. |
| 2 | Selecciona un nuevo rol del desplegable y pulsa "Actualizar". | Verifica que el rol seleccionado sea diferente y no vacío. |
| 3 | | Envía petición de actualización (`adminRepository.updateUserRole`). |
| 4 | | Muestra Toast Success: "Rol actualizado exitosamente". |
| 5 | | Recarga la lista de usuarios para reflejar el cambio. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Pulsa "Cancelar" en el modal. | Cierra el modal sin realizar cambios. |
| 2 | Selecciona el mismo rol que ya tenía. | El sistema no realiza ninguna petición al servidor. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de red al actualizar. | Muestra Toast Error: "Error al actualizar rol". |
| 2 | Intenta guardar sin seleccionar rol. | El validador del modal muestra: "Debes seleccionar un rol". |
---
## CU-003: Registro de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-003 |
| **Nombre** | Registro de usuarios |
| **Descripción** | Registro de nuevos usuarios con validación exhaustiva de datos personales y de cuenta. |
| **Actores** | Administrador / Usuario Invitado |
| **Pre condiciones** | N/A |
| **Post Condiciones** | Usuario creado en estado pendiente de verificación (o activo según config). Redirección a Login. |
| **Referencia a requisitos** | RF-003 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Completa form: Nombre, Apellido, ID, Teléfono, Dirección, Usuario, Email, Clave. | Valida formatos en tiempo real (regex para nombres, longitud de ID). |
| 2 | Pulsa "Registrarse". | Verifica coincidencia de contraseñas y campos obligatorios (`validateFormOnSubmit`). |
| 3 | | Envía datos a `authService.register` (excluyendo confirmPassword). |
| 4 | | Muestra Toast Success: "Usuario registrado exitosamente...". |
| 5 | | Redirige a la pantalla de Inicio de Sesión (`/login`). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona "Tipo ID: RUT" (13 dígitos). | Valida longitud exacta de 13 dígitos numéricos. |
| 2 | Ingresa teléfono con caracteres texto. | Elimina caracteres no numéricos automáticamente o muestra error. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Nombre/Apellido < 2 chars. | Borde rojo en input y texto: "El nombre debe tener al menos 2 caracteres". |
| 2 | Cédula longitud incorrecta (≠10). | "La cédula debe tener exactamente 10 caracteres numéricos". |
| 3 | Contraseña débil. | "Debe contener mayúscula, minúscula, número y especial". |
| 4 | Email / Usuario ya existe. | Toast Error desde backend: "El correo ya está en uso" (o mensaje del API). |
| 5 | Rate Limit (muchos intentos). | Toast Error: "Demasiados intentos. Por favor, espera...". |
---
## CU-004: Modificación de datos de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-004 |
| **Nombre** | Modificación de datos de usuarios |
| **Descripción** | Edición de perfil de usuario incluyendo nombre de usuario, email, estado activo/inactivo e imagen. |
| **Actores** | Administrador |
| **Pre condiciones** | Usuario seleccionado para editar. |
| **Post Condiciones** | Datos actualizados. |
| **Referencia a requisitos** | RF-004 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Pulsa "Editar" en un usuario. | Abre modal `EditUserModal` con datos precargados. |
| 2 | Modifica Email y cambia estado a "Inactivo". | Valida formato de email. Actualiza estado visual del botón (Rojo/Verde). |
| 3 | Pulsa "Guardar". | Envía petición `authService.updateUser`. |
| 4 | | Si cambió el rol, envía petición adicional `updateRole`. |
| 5 | | Cierra modal y actualiza la vista padre (`onUpdated`). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Pulsa botón de "Estado". | Alterna visualmente entre "Activo" (Verde) e "Inactivo" (Rojo). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Falla en actualización. | Muestra `alert("Hubo un error al actualizar el usuario.")`. |
---
## CU-005: Listado de usuarios
| Campo | Descripción |
|---|---|
| **Identificador** | CU-005 |
| **Nombre** | Listado de usuarios |
| **Descripción** | Visualización paginada y filtrable de todos los usuarios registrados en el sistema. |
| **Actores** | Administrador |
| **Pre condiciones** | Login como Admin. |
| **Post Condiciones** | Tabla cargada con datos. |
| **Referencia a requisitos** | RF-005 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a "Gestión de Usuarios". | Muestra skeleton loader ("Cargando usuarios..."). |
| 2 | | Realiza petición `adminRepository.listUsers(page, size)`. |
| 3 | | Renderiza tabla con: ID, Username, Email, Rol (Badge de color), Estado. |
| 4 | Cambia filtro de Rol. | Recarga la tabla filtrando por el rol seleccionado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No hay usuarios en la base de datos. | Muestra icono de Usuarios vacío y texto "No hay usuarios registrados". |
| 2 | Navega a siguiente página. | Carga siguiente lote de usuarios (Paginación). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de conexión al cargar. | Toast Error: "Error al cargar usuarios". Lista vacía. |
