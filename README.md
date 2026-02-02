---
title: "Casos de Uso - Grupo 3"
format: html
---
## CU-010: Consulta de Historial Médico del Atleta
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-010 |
| **Nombre** | Consulta de Historial Médico del Atleta |
| **Descripción** | Permite al entrenador acceder a la información médica confidencial de un atleta específico. |
| **Actores** | Entrenador |
| **Pre condiciones** | Entrenador autenticado y en el módulo de Directorio de Atletas (`HistorialMedicoPage`). |
| **Post Condiciones** | Se visualiza el detalle médico en un modal. |
| **Referencia a requisitos** | RF-010 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Busca al atleta en la lista y presiona botón "VER HISTORIAL". | Realiza petición al backend (`AtletaService.getHistorialByUserId`). |
| 2 | | Abre modal mostrando: Peso, Talla, IMC, Alergias, Enfermedades Hereditarias y Otras Enfermedades. |
| 3 | Presiona "Cerrar" o la 'X'. | Cierra el modal y regresa a la lista. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona atleta sin historial registrado. | Toast Error: "Aún no se ha registrado el historial médico". No abre el modal. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de conexión (Backend caído). | Toast Error: "Error al obtener el historial médico". |
---
## CU-011: Registro de baremos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-011 |
| **Nombre** | Registro de baremos |
| **Descripción** | Permite crear nuevos esquemas de puntuación (Baremos) asociados a una prueba, definiendo rangos de edad, sexo y clasificación. |
| **Actores** | Entrenador (o Admin según módulo Competencia) |
| **Pre condiciones** | En Módulo de Baremos. Pruebas deben existir previamente. |
| **Post Condiciones** | Nuevo baremo guardado y activo. |
| **Referencia a requisitos** | RF-011 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona "Añadir Baremo". | Abre modal `BaremoModal` con formulario vacío. |
| 2 | Selecciona Prueba, Sexo (M/F), Edad Mín/Máx. | Carga lista de pruebas disponibles. |
| 3 | Agrega rangos (Marca Mínima, Marca Máxima, Clasificación). | Permite añadir múltiples filas dinámicamente. |
| 4 | Presiona "Crear Baremo". | Muestra confirmación SweetAlert ("¿Crear Baremo?"). |
| 5 | Confirma acción. | Valida datos, guarda (`baremoService.create`), cierra modal y recarga tabla. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Intenta guardar sin rangos. | Alert Error: "Agregue al menos un rango de calificación". |
| 2 | No selecciona prueba. | Alert Error: "Seleccione una prueba". |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error del servidor al guardar. | El sistema no confirma la creación y mantiene el modal abierto (o cierra sin éxito dependiendo del catch). |
---
## CU-012: Modificación de baremos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-012 |
| **Nombre** | Modificación de baremos |
| **Descripción** | Permite editar los parámetros de un baremo existente, incluyendo sus rangos y reglas. |
| **Actores** | Entrenador |
| **Pre condiciones** | Baremo existente en la lista. |
| **Post Condiciones** | Baremo actualizado. |
| **Referencia a requisitos** | RF-012 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona botón "Editar" (lápiz) en un baremo. | Abre `BaremoModal` precargando todos los datos (pruebas, items, edades). |
| 2 | Modifica valores (ej. cambia rangos o edades). | Actualiza el estado del formulario local. |
| 3 | Presiona "Guardar Cambios". | Muestra confirmación SweetAlert ("¿Actualizar Baremo?"). |
| 4 | Confirma. | Envía actualización (`baremoService.update`), muestra éxito y recarga. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela la edición. | Cierra modal sin guardar cambios. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Baremo no encontrado (concurrencia). | Error de API (posiblemente atrapado en consola). |
---
## CU-013: Listado de baremos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-013 |
| **Nombre** | Listado de baremos |
| **Descripción** | Visualización tabular de los baremos registrados incluyendo prueba asociada, contexto (sexo/edad) y estado. |
| **Actores** | Entrenador |
| **Pre condiciones** | Acceso al módulo. |
| **Post Condiciones** | Tabla cargada. |
| **Referencia a requisitos** | RF-013 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a "Administración de Baremos". | Muestra indicador de carga ("Cargando Baremos..."). |
| 2 | | Obtiene datos (`baremoService.getAll`). |
| 3 | | Renderiza tabla con columnas: Prueba, Contexto (Sexo/Edad), Rangos (Conteo), Estado, Acciones. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No hay datos. | Muestra icono de caja vacía y texto "No hay baremos registrados". |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Fallo de red. | Se queda en estado de carga o muestra tabla vacía (error logueado en consola). |
---
## CU-014: Búsqueda de baremos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-014 |
| **Nombre** | Búsqueda de baremos |
| **Descripción** | Permite localizar baremos específicos. |
| **Actores** | Entrenador |
| **Pre condiciones** | Estar en el listado de baremos. |
| **Post Condiciones** | Identificación del baremo deseado. |
| **Referencia a requisitos** | RF-014 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Navega visualmente por la tabla ("Administración de Baremos"). | El sistema presenta todos los baremos ordenados. |
| 2 | (Nota: Funcionalidad de filtrado por texto no implementada en UI actual). | (El usuario debe buscar manualmente en la lista o usar la búsqueda del navegador). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | N/A | N/A |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | N/A | N/A |
---
## CU-015: Activar/desactivar baremos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-015 |
| **Nombre** | Activar/desactivar baremos |
| **Descripción** | Cambio lógico del estado de un baremo para habilitarlo o inhabilitarlo sin eliminarlo. |
| **Actores** | Entrenador |
| **Pre condiciones** | Baremo existente. |
| **Post Condiciones** | Estado del baremo invertido. |
| **Referencia a requisitos** | RF-015 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona el icono de estado (Check o Bloqueo) en la columna Acciones. | Muestra SweetAlert de advertencia: "¿Desea activar/desactivar el baremo...?". |
| 2 | Selecciona "Sí, activar" o "Sí, desactivar". | Llama a `baremoService.update` cambiando el booleano `estado`. |
| 3 | | Actualiza inmediatamente el icono y fondo de la fila (Opacidad para inactivos). Muestra SweetAlert "¡Éxito!". |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela en la alerta. | No realiza cambios. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error al guardar estado. | SweetAlert Error: "Error al cambiar el estado del baremo". |
