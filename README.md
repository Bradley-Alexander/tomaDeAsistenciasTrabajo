---
title: "Casos de Uso - Grupo 2"
format: html
---
## CU-006: Búsqueda de usuarios
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-006 |
| **Nombre** | Búsqueda de usuarios |
| **Descripción** | Permite al administrador localizar usuarios específicos mediante filtros de texto. |
| **Actores** | Administrador |
| **Pre condiciones** | El administrador debe haber iniciado sesión y encontrarse en el módulo de Gestión de Roles/Usuarios. |
| **Post Condiciones** | La lista de usuarios se filtra mostrando solo las coincidencias. |
| **Referencia a requisitos** | RF-006 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona la barra de búsqueda. | Habilita el cursor en el campo de texto. |
| 2 | Escribe un criterio (Ej: nombre o email). | Filtra la tabla en tiempo real (o al presionar Enter) buscando coincidencias parciales en **Nombre de Usuario** o **Correo Electrónico**. |
| 3 | | Muestra los resultados coincidentes en la tabla. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Escribe un criterio que no coincide con ningún usuario. | Muestra la tabla vacía o un mensaje "No hay usuarios para mostrar". |
| 2 | Borra el texto de búsqueda. | Restaura la lista completa de usuarios originales. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Caracteres inválidos en búsqueda. | El sistema los ignora o filtra literalmente sin encontrar resultados. |
---
## CU-007: Activar/desactivar usuario
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-007 |
| **Nombre** | Activar/desactivar usuario |
| **Descripción** | Permite dar de baja o reactivar el acceso de un usuario al sistema mediante el cambio de su estado. |
| **Actores** | Administrador |
| **Pre condiciones** | El usuario a modificar debe existir. |
| **Post Condiciones** | El estado del usuario cambia (Activo <-> Inactivo). Usuario inactivo no puede loguearse. |
| **Referencia a requisitos** | RF-007 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Accede a la edición del usuario (botón Editar). | Abre el modal `EditUserModal`. |
| 2 | Hace clic en el botón de "Estado del usuario" (Toggle). | Cambia visualmente el indicador: Verde (Activo) <-> Rojo (Inactivo). Texto cambia a "Activo"/"Inactivo". |
| 3 | Presiona "Guardar". | Envía la actualización al backend (`is_active: true/false`). |
| 4 | | Cierra el modal y actualiza el indicador de estado en la tabla lista de usuarios. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Desactiva su propio usuario (Admin). | El sistema podría permitirlo (riesgo) o bloquearlo según backend. (En UI actual: permite enviar la petición). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de persistencia. | Alert: "Hubo un error al actualizar el usuario". Estado no cambia. |
---
## CU-008: Registro de Atletas
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-008 |
| **Nombre** | Registro de Atletas |
| **Descripción** | Registro de nuevos usuarios con el rol de "Atleta", capturando información personal e institucional. |
| **Actores** | Atleta (Usuario externo/institucional) |
| **Pre condiciones** | No estar autenticado. |
| **Post Condiciones** | Cuenta creada con rol ATLETA. |
| **Referencia a requisitos** | RF-008 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a la opción "Regístrate aquí". | Muestra formulario de registro (`RegisterPage`). |
| 2 | Completa Datos Personales: Nombre, Apellido, Fecha Nacimiento, Sexo, ID, Teléfono, Dirección. | Valida formatos (longitud, numérico). |
| 3 | Completa Datos de Cuenta: Selecciona Estamento, Rol "Atleta", Usuario, Email, Clave. | Valida unicidad de usuario/email en backend al enviar. |
| 4 | Presiona "Registrarse". | Crea la cuenta. Muestra "Usuario registrado exitosamente". |
| 5 | | Redirige al Login. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona Rol diferente a Atleta (si está disponible). | El sistema crea el usuario con el rol seleccionado (Representante, etc.). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Faltan datos obligatorios. | Impide envío. Muestra mensajes de "Campo requerido" bajo cada input. |
| 2 | Fecha de nacimiento inválida. | Muestra error de validación HTML5. |
| 3 | Nota sobre datos físicos. | *Nota técnica: Los campos Peso, Talla y Experiencia descritos en el requisito no se solicitan en el formulario de registro actual del sistema.* |
---
## CU-009: Consulta de Historial Deportivo Propio
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-009 |
| **Nombre** | Consulta de Historial Deportivo Propio |
| **Descripción** | Permite al atleta visualizar sus estadísticas acumuladas y el desglose de resultados en competencias pasadas. |
| **Actores** | Atleta |
| **Pre condiciones** | Atleta autenticado en el sistema. |
| **Post Condiciones** | Visualización de datos actualizados. |
| **Referencia a requisitos** | RF-009 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Accede al Dashboard (`/dashboard/atleta`). | Carga datos vía `AtletaService.getEstadisticas()` y `getHistorial()`. |
| 2 | | Muestra tarjetas con conteo de Medallas (Oro/Plata/Bronce), Total Competencias, Años Experiencia y % Rendimiento. |
| 3 | Desplaza hacia abajo a "Historial de Competencias". | Muestra tabla con: Fecha, Competencia, Prueba, Resultado (Valor + Unidad), Posición (Badge) y Estado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No tiene historial registrado. | Muestra las tarjetas estadísticas en 0 y el mensaje "No hay resultados registrados aún" en la tabla. |
| 2 | Visualiza eventos futuros. | Muestra sección "Próximos Eventos" (actualmente con mensaje de "Próximamente"). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Fallo al cargar datos. | Toast Error: "Error al cargar los datos del dashboard". Spinner desaparece, datos se muestran vacíos o incompletos. |
