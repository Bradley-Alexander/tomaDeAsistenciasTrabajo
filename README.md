## CU-036: Modificación de baremos específicos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-036 |
| **Nombre** | Modificación de baremos específicos |
| **Descripción** | Permite al entrenador editar los rangos, valores y clasificaciones de un baremo específico asignado a una prueba. |
| **Actores** | Entrenador |
| **Pre condiciones** | El baremo específico debe existir y estar registrado en el sistema. |
| **Post Condiciones** | Los datos del baremo quedan actualizados en la base de datos. |
| **Referencia a requisitos** | RF-036 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | En el listado de baremos, identifica el registro a modificar y presiona el botón "Editar" (icono de lápiz). | El sistema abre el modal de edición (`BaremoModal`) cargando la información actual del baremo (Prueba asociada, rangos de marcas, clasificaciones). |
| 2 | Modifica los campos deseados (Ej. ajusta el rango máximo de una categoría o cambia la etiqueta de clasificación). | El sistema valida instantáneamente el formato de los datos ingresados en el formulario. |
| 3 | Presiona el botón "Guardar Cambios". | El sistema muestra una alerta de confirmación. |
| 4 | Confirma la operación. | El sistema envía la petición de actualización al servidor (`baremoService.update`). |
| 5 | | Al recibir respuesta exitosa, el sistema cierra el modal, muestra un mensaje de "Éxito" y actualiza la tabla con los nuevos datos. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Decide cancelar la modificación y presiona "Cancelar" o cierra el modal. | El sistema descarta los cambios no guardados y cierra la ventana modal. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Intenta guardar rangos incoherentes (Mín > Máx). | El sistema muestra un mensaje de validación "El valor mínimo no puede ser mayor al máximo" y no permite guardar. |
| 2 | Error de servidor (500). | El sistema muestra una alerta indicando "Error al actualizar el baremo" y mantiene los datos previos. |
---
## CU-037: Listado de baremos específicos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-037 |
| **Nombre** | Listado de baremos específicos |
| **Descripción** | Muestra una vista tabular de todos los baremos específicos configurados, detallando su clasificación y rangos. |
| **Actores** | Entrenador |
| **Pre condiciones** | Acceso al módulo de Baremos. |
| **Post Condiciones** | N/A |
| **Referencia a requisitos** | RF-037 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Ingresa a la sección "Baremos". | El sistema realiza una petición (`GET`) para obtener todos los baremos registrados. |
| 2 | | El sistema renderiza una tabla mostrando: Nombre de la Prueba, Contexto (Sexo/Edad), Clasificación (A/B/C...), Rango Máximo/Mínimo y Estado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | No existen baremos registrados en la base de datos. | El sistema muestra un estado vacío con el mensaje "No hay baremos registrados". |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | Fallo de conexión o tiempo de espera agotado. | El sistema muestra un indicador de carga indefinido o un mensaje de error "No se pudieron cargar los datos". |
---
## CU-038: Búsqueda de baremos específicos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-038 |
| **Nombre** | Búsqueda de baremos específicos |
| **Descripción** | Permite filtrar el listado de baremos por nombre de prueba o identificador del baremo. |
| **Actores** | Entrenador |
| **Pre condiciones** | Listado de baremos con datos cargados. |
| **Post Condiciones** | Listado filtrado según criterio. |
| **Referencia a requisitos** | RF-038 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Introduce el nombre de una prueba (Ej. "100m") en la barra de búsqueda superior. | El sistema filtra dinámicamente las filas de la tabla en tiempo real. |
| 2 | | El sistema muestra únicamente los baremos cuya prueba asociada o nombre coincida con el texto ingresado. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Borra el texto de búsqueda. | El sistema restaura el listado completo original. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | No se encuentran coincidencias. | El sistema muestra la tabla vacía con un mensaje "No se encontraron resultados para su búsqueda". |
---
## CU-039: Activar/desactivar baremos específicos
| Campo | Descripción |---|
|---|---|---|
| **Identificador** | CU-039 |
| **Nombre** | Activar/desactivar baremos específicos |
| **Descripción** | Permite habilitar o inhabilitar un baremo específico sin eliminarlo del sistema, controlando su disponibilidad para pruebas. |
| **Actores** | Entrenador |
| **Pre condiciones** | Baremo existente. |
| **Post Condiciones** | Estado del baremo modificado (True/False). |
| **Referencia a requisitos** | RF-039 |
**Flujo normal de eventos:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Presiona el botón de acción "Activar" (Check) o "Desactivar" (Bloqueo) en la fila del baremo deseado. | El sistema muestra una ventana de confirmación "¿Desea cambiar el estado del baremo?". |
| 2 | Confirma la acción seleccionando "Sí". | El sistema envía la petición de actualización al servidor. |
| 3 | | El sistema actualiza el indicador visual de estado ( Verde = Activo, Rojo = Inactivo) y emite una notificación de éxito. |
**Flujo alterno:**
| # | Actor (Acción) | Sistema (Reacción) |
|---|---|---|
| 1 | Rechaza la confirmación. | El sistema cancela la operación y no modifica el estado del registro. |
**Errores:**
| # | Error | Sistema (Mensaje/Acción) |
|---|---|---|
| 1 | El registro está bloqueado o eliminado. | El sistema muestra un error "No se pudo cambiar el estado" y refresca la vista para mostrar la información actual. |
