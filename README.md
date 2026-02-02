## CU-016: Clasificación de Resultados por Baremos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-016 |
| **Nombre** | Clasificación de Resultados por Baremos |
| **Descripción** | Asignación automática o visualización de la etiqueta cualitativa (Ej. Muy Bueno, Regular) basada en la marca obtenida y el baremo. |
| **Actores** | Entrenador |
| **Pre condiciones** | Existencia de resultados registrados. |
| **Post Condiciones** | Visualización de la clasificación en el listado de resultados. |
| **Referencia a requisitos** | RF-016 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Accede al listado de resultados en "Resultados de Pruebas". | El sistema lista los registros. La columna "Clasificación Final" muestra la etiqueta calculada (Ej. "AVANZADO", "PRINCIPIANTE") según el baremo y la marca. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Registra un nuevo resultado. | El sistema calcula internamente la clasificación comparando la marca con el baremo seleccionado y la guarda. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Baremo no configurado para la marca (fuera de rango). | El sistema muestra "Sin Clasificación" o deja el campo vacío en la columna correspondiente. |
---
## CU-017: Registro de entrenamiento (Test de Rendimiento)
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-017 |
| **Nombre** | Registro de entrenamiento (Test de Rendimiento) |
| **Descripción** | Registro de la aplicación de un test físico a un atleta, guardando la marca obtenida (tiempo, distancia) para su posterior evaluación. |
| **Actores** | Entrenador, Pasante |
| **Pre condiciones** | Atleta y Prueba deben existir. |
| **Post Condiciones** | Resultado guardado. |
| **Referencia a requisitos** | RF-017 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | En "Resultados de Pruebas", presiona "+ Nuevo Resultado". | Abre modal `RegistroPruebaModal`. |
| 2 | Selecciona Atleta, Competencia (Opcional), Prueba y Baremo. | Carga listas dinámicas. Muestra la unidad de medida según la prueba (s, m). |
| 3 | Ingresa la "Marca Obtenida". | Valida formato numérico. |
| 4 | Presiona "Guardar". | Envía datos a `resultadoPruebaService`. |
| 5 | | Muestra éxito, cierra modal y añade fila a la tabla. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela el registro presionando "Cancelar" o la 'X'. | El sistema cierra el modal sin guardar ningún dato. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de validación (backend) por datos faltantes. | Muestra mensaje de alerta (SweetAlert) indicando el error específico (Ej. "Faltan campos obligatorios"). |
| 2 | Error de conexión al guardar. | Muestra mensaje "No se pudo guardar", manteniendo el modal abierto para reintentar. |
---
## CU-018: Modificar entrenamiento (Test de Rendimiento)
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-018 |
| **Nombre** | Modificar entrenamiento |
| **Descripción** | Corrección de datos de un test ya registrado. |
| **Actores** | Entrenador, Pasante |
| **Pre condiciones** | Registro existente. |
| **Post Condiciones** | Datos actualizados. |
| **Referencia a requisitos** | RF-018 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona "Editar" en una fila de la tabla de resultados. | Abre el modal con los datos precargados (Atleta, Prueba, Marca). |
| 2 | Modifica la marca u otro campo. | Valida cambios localmente. |
| 3 | Presiona "Guardar". | Actualiza el registro en base de datos. Recarga la tabla. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Decide no realizar cambios y presiona "Cancelar". | El sistema cierra el modal manteniendo los datos originales intactos. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Registro no encontrado (eliminado por otro usuario). | El sistema muestra un error "No se pudo actualizar" y refresca la tabla. |
| 2 | Datos inválidos (marca negativa). | El sistema impide el envío y muestra error de validación en el formulario. |
---
## CU-019: Lista entrenamiento (Tests Realizados)
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-019 |
| **Nombre** | Lista entrenamiento |
| **Descripción** | Visualización histórica de tests aplicados. |
| **Actores** | Entrenador, Pasante |
| **Pre condiciones** | Acceso al módulo. |
| **Post Condiciones** | Tabla visible. |
| **Referencia a requisitos** | RF-019 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa al módulo "Resultados de Pruebas". | Muestra indicador de "Cargando...". |
| 2 | | Obtiene y renderiza tabla con: ID, Nombre Atleta, Prueba, Baremo, Marca, Clasificación, Fecha y Estado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No existen registros en la base de datos. | El sistema muestra un mensaje en la tabla: "No hay datos". |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Fallo de conexión con el servidor. | El sistema muestra mensaje de error en consola o notificación "Error cargando datos" y la tabla permanece vacía o en estado de carga infinito. |
---
## CU-020: Búsqueda de entrenamiento
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-020 |
| **Nombre** | Búsqueda de entrenamiento |
| **Descripción** | Localización de resultados específicos de un atleta o fecha. |
| **Actores** | Entrenador, Pasante |
| **Pre condiciones** | Listado cargado. |
| **Post Condiciones** | Registro localizado. |
| **Referencia a requisitos** | RF-020 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | El usuario navega visualmente (scroll) por la tabla de resultados. | El sistema mantiene el listado ordenado (generalmente por ID o Fecha) facilitando la localización. |
| 2 | Encuentra la fila correspondiente al atleta o fecha deseada. | El usuario procede a realizar la acción requerida (Editar/Activar). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | El usuario utiliza la función de búsqueda del navegador (Ctrl+F). | El navegador resalta las coincidencias de texto en la tabla visible. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | El registro buscado no se encuentra en la página actual (si hubiera paginación). | El usuario no encuentra el dato (Limitación actual: Sin barra de búsqueda server-side implementada). |
---
## CU-021: Activar/desactivar entrenamiento
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-021 |
| **Nombre** | Activar/desactivar entrenamiento |
| **Descripción** | Cambio de estado (lógico) de un resultado. |
| **Actores** | Entrenador, Pasante |
| **Pre condiciones** | Registro existente. |
| **Post Condiciones** | Estado cambiado (Activar <-> Desactivar). |
| **Referencia a requisitos** | RF-021 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Identifica un registro y presiona el botón "Activar" o "Desactivar" en la columna de acciones. | Realiza petición al backend para invertir el estado booleano de `estado`. |
| 2 | | Recarga la tabla mostrando el nuevo estado (TRUE/FALSE) y cambiando el color del indicador (Verde/Rojo). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | El usuario desea revertir el cambio inmediatamente. | Vuelve a presionar el botón (ahora con el texto opuesto) y el sistema restaura el estado original. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error al procesar la solicitud. | El sistema muestra una alerta "No se pudo cambiar estado" y mantiene el estado visual anterior. |
---
## CU-022: Seguimiento de rendimiento
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-022 |
| **Nombre** | Seguimiento de rendimiento |
| **Descripción** | Visualización gráfica y estadística de la evolución del atleta. |
| **Actores** | Entrenador, Pasante |
| **Pre condiciones** | Resultados registrados. |
| **Post Condiciones** | Visualización de evolución. |
| **Referencia a requisitos** | RF-022 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a "Métricas de Rendimiento" (`RendimientoPage`). | Carga gráficos generales (Top 10 marcas). |
| 2 | Selecciona pestaña "Individual". | Muestra selector ("dropdown") de atletas. |
| 3 | Selecciona un atleta específico en el menú desplegable. | Genera y muestra gráfico de linea "Historial de Rendimiento" (Eje Y: Puntaje/Marca, Eje X: Fecha). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Selecciona un atleta que no tiene resultados registrados. | El sistema muestra un mensaje informativo: "No hay resultados registrados para este atleta". Los gráficos no se renderizan. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Fallo en la carga de datos (API error). | El sistema pantalla de error: "Error de Carga" con botón "Reintentar". |
| 2 | Error de renderizado en gráficos (datos corruptos). | El componente de gráfico puede mostrarse en blanco o con mensaje de error de la librería (console log). |
---
## CU-023: Registro de pruebas
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-023 |
| **Nombre** | Registro de pruebas |
| **Descripción** | Creación de nuevas definiciones de pruebas atléticas (Ej. 100m Planos) asociadas a una disciplina y baremo base. |
| **Actores** | Entrenador |
| **Pre condiciones** | Disciplinas existentes. |
| **Post Condiciones** | Nueva prueba disponible para registro de resultados. |
| **Referencia a requisitos** | RF-023 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | En "Gestión de Pruebas", presiona "Nueva Prueba". | Abre modal `PruebaModal`. |
| 2 | Ingresa Nombre, Siglas, Tipo (Normal/Competencia), selecciona Tipo Disciplina y Unidad Medida. | Valida campos requeridos. |
| 3 | Presiona "Guardar". | Envía datos (`pruebaService.create`). |
| 4 | | Muestra mensaje de éxito, cierra modal y añade la nueva prueba a la lista. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cierra el modal antes de guardar. | Cancela la operación sin guardar datos. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Intenta registrar prueba con siglas ya existentes (duplicado). | El sistema (backend) rechaza la solicitud y muestra alerta de error (SweetAlert). |
| 2 | Datos inválidos. | Alerta indicando "Error de validación". |
---
## CU-024: Modificar pruebas
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-024 |
| **Nombre** | Modificar pruebas |
| **Descripción** | Edición de título, siglas o configuración de una prueba. |
| **Actores** | Entrenador |
| **Pre condiciones** | Prueba existente. |
| **Post Condiciones** | Datos actualizados. |
| **Referencia a requisitos** | RF-024 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona "Editar" (lápiz) en la lista de pruebas. | Abre modal con datos actuales precargados. |
| 2 | Modifica campos (Ej. corrige el nombre o cambia siglas). | Valida formato. |
| 3 | Presiona "Guardar Cambios". | Confirma y envía actualización al servidor. |
| 4 | | Refresca la tabla mostrando los datos nuevos. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela la edición. | Cierra el modal y mantiene datos originales. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de servidor al actualizar. | Muestra alerta de error y mantiene los datos antiguos en la base de datos. |
---
## CU-025: Listado de pruebas
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-025 |
| **Nombre** | Listado de pruebas |
| **Descripción** | Visualización del catálogo de pruebas configuradas. |
| **Actores** | Entrenador |
| **Pre condiciones** | N/A |
| **Post Condiciones** | N/A |
| **Referencia a requisitos** | RF-025 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Accede a "Gestión de Pruebas". | Muestra pantalla de carga ("Sincronizando datos..."). |
| 2 | | Renderiza tabla con: Siglas, Nombre, Tipo, Disciplina asociada, Clase de Baremo y Estado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No existen pruebas registradas. | Muestra mensaje e icono de "No hay pruebas registradas" en lugar de la tabla. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de conexión. | El indicador de carga permanece indefinidamente o se muestra un error de red en consola (la UI no tiene un estado de error explícito visual implementado aparte del log). |
