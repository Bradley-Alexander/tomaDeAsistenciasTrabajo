---
title: "Casos de Uso - Grupo 5"
format: html
---
## CU-026: Búsqueda de pruebas
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-026 |
| **Nombre** | Búsqueda de pruebas |
| **Descripción** | Permite al entrenador localizar pruebas específicas por nombre o baremo asociado. |
| **Actores** | Entrenador |
| **Pre condiciones** | Listado de pruebas cargado. |
| **Post Condiciones** | Prueba localizada. |
| **Referencia a requisitos** | RF-026 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa al módulo "Gestión de Pruebas". | Muestra el listado de todas las pruebas configuradas. |
| 2 | (Nota: Funcionalidad de búsqueda no implementada en UI actual). El usuario navega visualmente por la lista. | El sistema mantiene el ordenamiento por defecto (generalmente fecha de carga). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Utiliza la función de búsqueda de texto del navegador (Ctrl+F). | El navegador resalta las coincidencias (Ej. "100m", "Fuerza"). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | La prueba no existe en la página actual. | El usuario no encuentra el ítem (Limitación de paginación/filtrado). |
---
## CU-027: Activar/desactivar pruebas
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-027 |
| **Nombre** | Activar/desactivar pruebas |
| **Descripción** | Permite cambiar el estado de disponibilidad de una prueba. |
| **Actores** | Entrenador |
| **Pre condiciones** | Prueba existente. |
| **Post Condiciones** | Estado actualizado (Activo/Inactivo). |
| **Referencia a requisitos** | RF-027 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona el botón de estado (Check/Block) en la fila de la prueba. | Muestra alerta de confirmación (SweetAlert): "¿Desea activar/desactivar la prueba...?". |
| 2 | Confirma la acción. | Envía petición al servidor (`pruebaService.update`). |
| 3 | | Actualiza el icono y el estilo de la fila inmediatamente. Muestra mensaje de éxito. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela la confirmación. | Cierra la alerta sin realizar cambios. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de conexión o servidor. | Muestra alerta de error y revierte (o no aplica) el cambio visual. |
---
## CU-028: Generación de reportes individuales y globales
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-028 |
| **Nombre** | Generación de reportes individuales y globales |
| **Descripción** | Exportación de datos estadísticos y operativos a formatos portables (PDF/Excel). |
| **Actores** | Entrenador |
| **Pre condiciones** | Acceso a módulos de Asistencia o Rendimiento con datos. |
| **Post Condiciones** | Archivo descargado. |
| **Referencia a requisitos** | RF-028 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | En "Gestión de Asistencia" o "Reportes", presiona "Exportar Reporte" (Botón visual). | (Implementación pendiente en JS: Debería generar el blob del archivo). |
| 2 | | Inicia la descarga del archivo generado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No hay datos para exportar. | El sistema genera un reporte vacío o muestra alerta "Sin datos". |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Fallo en la generación del PDF. | El botón no responde o muestra error en consola. |
---
## CU-029: Filtro de atletas por categoría, género y rendimiento
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-029 |
| **Nombre** | Filtro de atletas |
| **Descripción** | Búsqueda segmentada de atletas en el directorio. |
| **Actores** | Entrenador |
| **Pre condiciones** | Listado de atletas cargado. |
| **Post Condiciones** | Lista filtrada mostrada. |
| **Referencia a requisitos** | RF-029 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a "Atletas". Usa los controles de filtro (Categoría, Género). | (Implementación actual en `AthletesTable` usa barra de búsqueda general y pestañas/filtros básicos). Filtra la tabla dinámicamente. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Ningún atleta cumple los criterios. | Muestra tabla vacía o mensaje "No se encontraron atletas". |
---
## CU-030: Registro de asistencia a entrenamientos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-030 |
| **Nombre** | Registro de asistencia a entrenamientos |
| **Descripción** | Control de presencia de atletas en una sesión específica. |
| **Actores** | Entrenador |
| **Pre condiciones** | Entrenamiento y Horario creados. Atletas inscritos. |
| **Post Condiciones** | Asistencia registrada (Presente/Ausente). |
| **Referencia a requisitos** | RF-030 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a la sesión (`GestionAsistenciaPage`). | Muestra lista de inscritos con su estado actual. |
| 2 | Localiza un atleta con estado "Ausente" (Rojo) y presiona "Asistió" (Verde). | Envía petición (`AsistenciaService.marcarPresente` o `registrarAsistencia`). |
| 3 | | Actualiza la etiqueta a "Presente" (Verde) y recalcula contadores de asistencia. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Marca "Ausente" a un atleta que estaba "Presente". | El sistema actualiza el estado a Ausente. |
| 2 | Inscribe un nuevo atleta manualmente ("Inscribir Atleta"). | Abre modal, selecciona atleta, guarda y actualiza la lista. |
| 3 | Intenta marcar presente a un atleta que "No Asistirá" (Confirmado por atleta). | El botón está deshabilitado (lógica de negocio). |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error al registrar asistencia. | Notificación Toast Error: "Error al marcar como presente". |
---
## CU-031: Registro de competencias y resultados
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-031 |
| **Nombre** | Registro de competencias y resultados |
| **Descripción** | Creación de eventos competitivos y carga de marcas oficiales. |
| **Actores** | Entrenador |
| **Pre condiciones** | N/A |
| **Post Condiciones** | Competencia o Resultado creados. |
| **Referencia a requisitos** | RF-031 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | (Competencia) En "Gestión de Competencias", presiona "Crear Nueva Competencia". | Abre formulario (Nombre, Fecha, Lugar, Estado). |
| 2 | Completa y Guarda. | Crea competencia y actualiza lista. |
| 3 | (Resultado) En "Registro de Resultados", presiona "Registrar Resultado". | Abre formulario. |
| 4 | Selecciona Competencia, Atleta, Prueba, ingresa Marca, Posición. | Valida tipos de datos. |
| 5 | Guarda. | Registra resultado oficial vinculado. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Faltan campos obligatorios. | Muestra errores de validación en el formulario. |
---
## CU-032: Modificación de competencias y resultados
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-032 |
| **Nombre** | Modificación de competencias y resultados |
| **Descripción** | Edición de datos de eventos o marcas erróneas. |
| **Actores** | Entrenador |
| **Pre condiciones** | Registro existente. |
| **Post Condiciones** | Datos corregidos. |
| **Referencia a requisitos** | RF-032 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona "Editar" en la tabla correspondiente. | Abre modal con datos precargados. |
| 2 | Realiza cambios (Ej. corrige fecha o marca). | |
| 3 | Guarda. | Envía actualización y refresca la vista. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Cancela cambios. | Cierra modal sin guardar. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Error de servidor. | Muestra alerta de error. |
---
## CU-033: Listado de competencias y resultados
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-033 |
| **Nombre** | Listado de competencias y resultados |
| **Descripción** | Visualización centralizada de eventos y marcas. |
| **Actores** | Entrenador |
| **Pre condiciones** | Acceso al módulo. |
| **Post Condiciones** | Tablas visibles. |
| **Referencia a requisitos** | RF-033 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Accede a la página. | Carga datos desde API. |
| 2 | | Muestra tablas con columnas relevantes (Nombre, Fecha, Lugar / Atleta, Prueba, Marca). |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Tabla vacía. | Muestra mensaje gráfico "No hay datos registrados". |
---
## CU-034: Búsqueda de competencias y resultados
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-034 |
| **Nombre** | Búsqueda de competencias y resultados |
| **Descripción** | Filtrado de listas por nombre, fecha o atleta. |
| **Actores** | Entrenador |
| **Pre condiciones** | Listas con datos. |
| **Post Condiciones** | Resultados filtrados. |
| **Referencia a requisitos** | RF-034 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa texto en barras de búsqueda ("Buscar por nombre...", "Buscar por atleta..."). | |
| 2 | (Automático) El sistema filtra la lista en tiempo real (o al presionar Enter) mostrando solo coincidencias. | |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Sin coincidencias. | Muestra "No se encontraron resultados/competencias". |
---
## CU-035: Registro de baremos específicos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-035 |
| **Nombre** | Registro de baremos específicos |
| **Descripción** | Definición de rangos de clasificación con valores mínimos, máximos y etiquetas (A, B, C / Clasificación). |
| **Actores** | Entrenador |
| **Pre condiciones** | Prueba seleccionada. |
| **Post Condiciones** | Definición de baremo guardada. |
| **Referencia a requisitos** | RF-035 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | (Dentro de `BaremoModal` o conf. de prueba) Agrega una fila de clasificación. | Sistema habilita campos: Marca Min, Marca Max, Clasificación. |
| 2 | Ingresa valores (Ej. 10.0 - 12.0 = "A"). | |
| 3 | Guarda el conjunto. | Asocia la matriz de baremos a la prueba/categoría. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Elimina una fila de clasificación. | Quita el rango de la definición visual antes de guardar. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Rangos solapados (si hubiera validación). | Error "Los rangos no pueden superponerse". |
