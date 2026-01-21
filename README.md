# Casos de Prueba - Módulo Entrenador

## Descripción General
Este documento define los casos de prueba (FASE 1) para el módulo de Entrenador en la aplicación de Athletics. Incluye tres servicios principales: Entrenamiento, Horario y Asistencia. 

⚠️ **IMPORTANTE:** Los casos de prueba en este documento son el CONTRATO OFICIAL entre Frontend y Backend. Todos los JSON son 100% válidos y pueden ser copiados directamente en requests reales.

---

# MÓDULO: ENTRENAMIENTO

## FRONTEND - CREAR ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-01 | Crear entrenamiento válido | Registro de nuevo entrenamiento con todos los campos | Nombre: "Natación Nivel Avanzado", Descripción: "Entrenamiento de natación para atletas avanzados", Disciplina: "NATACION", Nivel: "AVANZADO", Capacidad: 20, Horarios: [] | Mensaje: "Entrenamiento creado exitosamente." Redirección a lista de entrenamientos. Nuevo entrenamiento visible en tabla. | Entrenador autenticado, API disponible | |
| TC-EN-02 | Crear con horarios | Crear entrenamiento con horarios incluidos | Nombre: "Atletismo Base", Descripción: "Base de atletismo", Disciplina: "ATLETISMO", Nivel: "PRINCIPIANTE", Capacidad: 30, Horarios: [{nombre: "Lunes", hora_inicio: "06:00", hora_fin: "07:00"}] | Mensaje: "Entrenamiento creado exitosamente." Entrenamiento y horarios guardados. | Entrenador autenticado | |
| TC-EN-03 | Nombre duplicado | Intento de crear con nombre ya existente | Nombre: "Natación Nivel Avanzado" (existe) | Toast error: "Ya existe un entrenamiento con este nombre." Formulario no se envía. | Entrenador autenticado, Entrenamiento duplicado existe | |
| TC-EN-04 | Campos obligatorios vacíos | Intento sin llenar campos requeridos | Nombre: (vacío), Disciplina: (vacío) | Toast error: "Los campos Nombre y Disciplina son obligatorios." Botón deshabilitado o validación visible. | | |
| TC-EN-05 | Capacidad inválida | Capacidad con valor no numérico o negativo | Capacidad: -5 | Toast error: "La capacidad debe ser un número positivo." Campo destacado en rojo. | | |

## FRONTEND - LISTAR ENTRENAMIENTOS

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-06 | Listar mis entrenamientos | Cargar lista de todos los entrenamientos del entrenador | Clic en menú "Mis Entrenamientos" | Tabla con columnas: Nombre, Disciplina, Nivel, Capacidad, Acciones (Ver, Editar, Eliminar). Ejemplo: Natación Nivel Avanzado \| NATACION \| AVANZADO \| 20 \| Ver Editar Eliminar | Entrenador autenticado, Entrenamientos creados | |
| TC-EN-07 | Lista vacía | Ver lista cuando no hay entrenamientos | Clic en menú "Mis Entrenamientos" | Mensaje informativo: "No tienes entrenamientos registrados." Botón "Crear Nuevo Entrenamiento" visible y destacado. | Entrenador autenticado, Sin entrenamientos | |
| TC-EN-08 | Buscar/Filtrar | Filtrar entrenamientos por disciplina | Seleccionar filtro Disciplina: "NATACION" | Tabla actualizada mostrando solo entrenamientos de NATACION. Contador: "2 entrenamientos encontrados". | Entrenador con múltiples entrenamientos | |

## FRONTEND - VER DETALLE ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-09 | Ver detalle | Abrir detalle completo de un entrenamiento | Clic en botón "Ver" en una fila | Modal/Página con: Nombre, Descripción, Disciplina, Nivel, Capacidad, Lista de Horarios, Sección de Atletas Registrados, Botones: Editar, Eliminar, Volver | Entrenador autenticado, Entrenamiento seleccionado existe | |
| TC-EN-10 | Detalle con horarios | Ver detalle incluyendo horarios | Ver detalle de entrenamiento con horarios | Sección "Horarios" con tabla: Nombre, Hora Inicio, Hora Fin, Acciones (Editar, Eliminar) | Entrenamiento con horarios creados | |

## FRONTEND - EDITAR ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-11 | Editar campos básicos | Modificar nombre y descripción | Nombre: "Natación Nivel Intermedio", Descripción: "Nuevo nivel intermedio" | Toast: "Entrenamiento actualizado exitosamente." Campos reflejados en lista y detalle. | Entrenador autenticado, Entrenamiento seleccionado | |
| TC-EN-12 | Cambiar capacidad | Aumentar/disminuir capacidad | Capacidad anterior: 20, Nueva: 25 | Toast: "Entrenamiento actualizado exitosamente." Nueva capacidad visible en lista. | | |
| TC-EN-13 | Editar a nombre duplicado | Intentar cambiar nombre a uno existente | Nombre: "Atletismo Base" (existe otro) | Toast error: "Ya existe un entrenamiento con este nombre." Cambio rechazado. | Otro entrenamiento con nombre existe | |

## FRONTEND - ELIMINAR ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-14 | Eliminar entrenamiento | Eliminar con confirmación | Clic en "Eliminar", Confirmar en modal | Modal: "¿Deseas eliminar este entrenamiento? Esta acción no se puede deshacer." Confirmar. Toast: "Entrenamiento eliminado exitosamente." Eliminado de lista. | Entrenador autenticado, Entrenamiento sin atletas | |
| TC-EN-15 | Eliminar con atletas registrados | Intento de eliminar con atletas | Clic en "Eliminar" | Toast error: "No puedes eliminar un entrenamiento con atletas registrados." Acción bloqueada. | Entrenamiento con atletas registrados | |

---

## BACKEND - CREAR ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-01 | Crear entrenamiento válido | POST /api/v1/entrenador/entrenamientos | `{"nombre":"Natación Nivel Avanzado","descripcion":"Entrenamiento de natación para atletas avanzados","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"horarios":[]}` | `{"success":true,"message":"Entrenamiento creado exitosamente.","data":{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","nombre":"Natación Nivel Avanzado","descripcion":"Entrenamiento de natación para atletas avanzados","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"entrenador_id":1,"horarios":[]},"errors":null}` (Status: 201) | Entrenador autenticado, Nombre único | Exitoso |
| TC-EN-02 | Crear con horarios | POST /api/v1/entrenador/entrenamientos | `{"nombre":"Atletismo Base","descripcion":"Base de atletismo","disciplina":"ATLETISMO","nivel":"PRINCIPIANTE","capacidad":30,"horarios":[{"nombre":"Lunes","hora_inicio":"06:00","hora_fin":"07:00"}]}` | `{"success":true,"message":"Entrenamiento creado exitosamente.","data":{"id":2,"external_id":"660e8400-e29b-41d4-a716-446655440001","nombre":"Atletismo Base","descripcion":"Base de atletismo","disciplina":"ATLETISMO","nivel":"PRINCIPIANTE","capacidad":30,"entrenador_id":1,"horarios":[{"id":1,"external_id":"770e8400-e29b-41d4-a716-446655440002","nombre":"Lunes","hora_inicio":"06:00","hora_fin":"07:00","entrenamiento_id":2}]},"errors":null}` (Status: 201) | Entrenador autenticado | Exitoso |
| TC-EN-03 | Nombre duplicado | POST /api/v1/entrenador/entrenamientos | `{"nombre":"Natación Nivel Avanzado","descripcion":"Descripción","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"horarios":[]}` | `{"success":false,"message":"Ya existe un entrenamiento con este nombre.","data":null,"errors":null}` (Status: 409) | Entrenamiento duplicado existe | Fallido |
| TC-EN-04 | Campos obligatorios faltantes | POST /api/v1/entrenador/entrenamientos | `{"nombre":"","descripcion":"","disciplina":"","nivel":"","capacidad":20,"horarios":[]}` | `{"success":false,"message":"Validation Error","data":null,"errors":[{"field":"nombre","message":"Campo requerido"},{"field":"disciplina","message":"Campo requerido"}]}` (Status: 422) | | Fallido |
| TC-EN-05 | Capacidad inválida | POST /api/v1/entrenador/entrenamientos | `{"nombre":"Test","descripcion":"Test","disciplina":"NATACION","nivel":"AVANZADO","capacidad":-5,"horarios":[]}` | `{"success":false,"message":"Validation Error","data":null,"errors":[{"field":"capacidad","message":"La capacidad debe ser un número positivo"}]}` (Status: 422) | | Fallido |

---

## BACKEND - LISTAR ENTRENAMIENTOS

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-06 | Listar entrenamientos | GET /api/v1/entrenador/entrenamientos | (Sin body) | `{"success":true,"message":"Entrenamientos obtenidos exitosamente.","data":[{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","nombre":"Natación Nivel Avanzado","descripcion":"Entrenamiento de natación para atletas avanzados","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"entrenador_id":1,"horarios":[{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440003","nombre":"Martes","hora_inicio":"08:00","hora_fin":"09:00","entrenamiento_id":1}]},{"id":2,"external_id":"660e8400-e29b-41d4-a716-446655440001","nombre":"Atletismo Base","descripcion":"Base de atletismo","disciplina":"ATLETISMO","nivel":"PRINCIPIANTE","capacidad":30,"entrenador_id":1,"horarios":[]}],"errors":null}` (Status: 200) | Entrenador autenticado, Entrenamientos creados | Exitoso |
| TC-EN-07 | Lista vacía | GET /api/v1/entrenador/entrenamientos | (Sin body) | `{"success":true,"message":"Entrenamientos obtenidos exitosamente.","data":[],"errors":null}` (Status: 200) | Entrenador autenticado, Sin entrenamientos | Exitoso |

---

## BACKEND - VER DETALLE ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-09 | Ver detalle | GET /api/v1/entrenador/entrenamientos/1 | (Sin body) | `{"success":true,"message":"Entrenamiento obtenido exitosamente.","data":{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","nombre":"Natación Nivel Avanzado","descripcion":"Entrenamiento de natación para atletas avanzados","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"entrenador_id":1,"horarios":[{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440003","nombre":"Martes","hora_inicio":"08:00","hora_fin":"09:00","entrenamiento_id":1}]},"errors":null}` (Status: 200) | Entrenador autenticado, Entrenamiento existe | Exitoso |
| TC-EN-10 | Entrenamiento no encontrado | GET /api/v1/entrenador/entrenamientos/999 | (Sin body) | `{"success":false,"message":"Entrenamiento no encontrado.","data":null,"errors":null}` (Status: 404) | Entrenador autenticado, Entrenamiento no existe | Fallido |
| TC-EN-11 | Sin autorización | GET /api/v1/entrenador/entrenamientos/1 (pertenece a otro entrenador) | (Sin body) | `{"success":false,"message":"No tienes permiso para acceder a este entrenamiento.","data":null,"errors":null}` (Status: 403) | Entrenador autenticado, Entrenamiento pertenece a otro | Fallido |

---

## BACKEND - EDITAR ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-12 | Editar exitoso | PUT /api/v1/entrenador/entrenamientos/1 | `{"nombre":"Natación Nivel Intermedio","descripcion":"Nuevo nivel intermedio","disciplina":"NATACION","nivel":"INTERMEDIO","capacidad":25,"horarios":[]}` | `{"success":true,"message":"Entrenamiento actualizado exitosamente.","data":{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","nombre":"Natación Nivel Intermedio","descripcion":"Nuevo nivel intermedio","disciplina":"NATACION","nivel":"INTERMEDIO","capacidad":25,"entrenador_id":1,"horarios":[]},"errors":null}` (Status: 200) | Entrenador autenticado, Entrenamiento existe | Exitoso |
| TC-EN-13 | Nombre duplicado en edición | PUT /api/v1/entrenador/entrenamientos/1 | `{"nombre":"Atletismo Base","descripcion":"","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"horarios":[]}` | `{"success":false,"message":"Ya existe un entrenamiento con este nombre.","data":null,"errors":null}` (Status: 409) | Otro entrenamiento con nombre existe | Fallido |
| TC-EN-14 | Sin autorización | PUT /api/v1/entrenador/entrenamientos/1 (pertenece a otro) | `{"nombre":"Test","descripcion":"Test","disciplina":"NATACION","nivel":"AVANZADO","capacidad":20,"horarios":[]}` | `{"success":false,"message":"No tienes permiso para editar este entrenamiento.","data":null,"errors":null}` (Status: 403) | Entrenador autenticado, Entrenamiento pertenece a otro | Fallido |

---

## BACKEND - ELIMINAR ENTRENAMIENTO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-EN-15 | Eliminar exitoso | DELETE /api/v1/entrenador/entrenamientos/1 | (Sin body) | `{"success":true,"message":"Entrenamiento eliminado exitosamente.","data":null,"errors":null}` (Status: 200) | Entrenador autenticado, Entrenamiento existe, Sin atletas registrados | Exitoso |
| TC-EN-16 | Con atletas registrados | DELETE /api/v1/entrenador/entrenamientos/1 | (Sin body) | `{"success":false,"message":"No puedes eliminar un entrenamiento con atletas registrados.","data":null,"errors":null}` (Status: 409) | Entrenamiento con atletas | Fallido |
| TC-EN-17 | Sin autorización | DELETE /api/v1/entrenador/entrenamientos/1 (pertenece a otro) | (Sin body) | `{"success":false,"message":"No tienes permiso para eliminar este entrenamiento.","data":null,"errors":null}` (Status: 403) | Entrenamiento pertenece a otro entrenador | Fallido |

---

# MÓDULO: HORARIO

## FRONTEND - CREAR HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-HR-01 | Crear horario válido | Crear nuevo horario para entrenamiento | Nombre: "Lunes Mañana", Hora Inicio: 08:00, Hora Fin: 09:00 | Toast: "Horario creado exitosamente." Horario visible en tabla. | Entrenador autenticado, Entrenamiento seleccionado | |
| TC-HR-02 | Horas inválidas | Hora inicio mayor o igual a hora fin | Hora Inicio: 10:00, Hora Fin: 08:00 | Toast error: "La hora de inicio debe ser anterior a la hora de fin." Formulario no se envía. | | |
| TC-HR-03 | Mismo horario duplicado | Horario con mismas horas y nombre | Nombre: "Lunes Mañana", Hora Inicio: 08:00, Hora Fin: 09:00 (existe igual) | Toast error: "Ya existe un horario con estos datos." | Horario exacto existe | |

## FRONTEND - LISTAR HORARIOS

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-HR-04 | Listar horarios | Ver todos los horarios de un entrenamiento | Seleccionar entrenamiento | Tabla con columnas: Nombre, Hora Inicio, Hora Fin, Acciones. Ejemplo: Lunes Mañana \| 08:00 \| 09:00 \| Editar Eliminar | Entrenador autenticado, Horarios creados | |
| TC-HR-05 | Lista vacía | Sin horarios creados | Ver lista vacía | Mensaje: "No hay horarios registrados para este entrenamiento." Botón "Crear Nuevo Horario" destacado. | Entrenamiento sin horarios | |

## FRONTEND - ELIMINAR HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-HR-06 | Eliminar exitoso | Eliminar horario existente | Clic en "Eliminar", Confirmar | Modal: "¿Deseas eliminar este horario?" Toast: "Horario eliminado exitosamente." Removido de tabla. | Entrenador autenticado, Horario existe | |
| TC-HR-07 | Eliminar sin permisos | Intento de eliminar horario de otro | Clic en "Eliminar" | Toast error: "No tienes permiso para eliminar este horario." Acción bloqueada. | Horario pertenece a otro entrenador | |

---

## BACKEND - CREAR HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-HR-01 | Crear horario válido | POST /api/v1/entrenador/horarios/entrenamiento/1 | `{"nombre":"Lunes Mañana","hora_inicio":"08:00","hora_fin":"09:00"}` | `{"success":true,"message":"Horario creado exitosamente.","data":{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","nombre":"Lunes Mañana","hora_inicio":"08:00","hora_fin":"09:00","entrenamiento_id":1},"errors":null}` (Status: 201) | Entrenador autenticado, Entrenamiento existe | Exitoso |
| TC-HR-02 | Horas inválidas | POST /api/v1/entrenador/horarios/entrenamiento/1 | `{"nombre":"Mal","hora_inicio":"10:00","hora_fin":"08:00"}` | `{"success":false,"message":"La hora de inicio debe ser anterior a la hora de fin.","data":null,"errors":null}` (Status: 400) | | Fallido |
| TC-HR-03 | Entrenamiento no encontrado | POST /api/v1/entrenador/horarios/entrenamiento/999 | `{"nombre":"Lunes Mañana","hora_inicio":"08:00","hora_fin":"09:00"}` | `{"success":false,"message":"Entrenamiento no encontrado o no autorizado.","data":null,"errors":null}` (Status: 404) | Entrenamiento no existe | Fallido |

---

## BACKEND - LISTAR HORARIOS

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-HR-04 | Listar horarios | GET /api/v1/entrenador/horarios/entrenamiento/1 | (Sin body) | `{"success":true,"message":"Horarios obtenidos exitosamente.","data":[{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","nombre":"Lunes Mañana","hora_inicio":"08:00","hora_fin":"09:00","entrenamiento_id":1},{"id":2,"external_id":"660e8400-e29b-41d4-a716-446655440001","nombre":"Martes Tarde","hora_inicio":"14:00","hora_fin":"15:00","entrenamiento_id":1}],"errors":null}` (Status: 200) | Entrenador autenticado, Horarios creados | Exitoso |
| TC-HR-05 | Lista vacía | GET /api/v1/entrenador/horarios/entrenamiento/1 | (Sin body) | `{"success":true,"message":"Horarios obtenidos exitosamente.","data":[],"errors":null}` (Status: 200) | Sin horarios | Exitoso |
| TC-HR-06 | Entrenamiento no encontrado | GET /api/v1/entrenador/horarios/entrenamiento/999 | (Sin body) | `{"success":false,"message":"Entrenamiento no encontrado o no autorizado.","data":null,"errors":null}` (Status: 404) | Entrenamiento no existe | Fallido |

---

## BACKEND - ELIMINAR HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-HR-07 | Eliminar exitoso | DELETE /api/v1/entrenador/horarios/1 | (Sin body) | `{"success":true,"message":"Horario eliminado exitosamente.","data":null,"errors":null}` (Status: 200) | Entrenador autenticado, Horario existe | Exitoso |
| TC-HR-08 | Horario no encontrado | DELETE /api/v1/entrenador/horarios/999 | (Sin body) | `{"success":false,"message":"Horario no encontrado.","data":null,"errors":null}` (Status: 404) | Horario no existe | Fallido |
| TC-HR-09 | Sin permisos | DELETE /api/v1/entrenador/horarios/1 (pertenece a otro) | (Sin body) | `{"success":false,"message":"No tienes permiso para eliminar este horario.","data":null,"errors":null}` (Status: 403) | Horario pertenece a otro entrenador | Fallido |

---

# MÓDULO: ASISTENCIA

## FRONTEND - REGISTRAR ATLETA EN HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-01 | Registrar atleta | Inscribir atleta en un horario | Seleccionar Atleta, Horario | Toast: "Atleta registrado exitosamente." Atleta aparece en lista de inscritos. | Entrenador autenticado, Atleta y Horario existen | |
| TC-AS-02 | Atleta ya inscrito | Intento de inscribir atleta ya inscrito | Seleccionar atleta duplicado | Toast error: "El atleta ya está registrado en este horario." | Atleta ya inscrito | |
| TC-AS-03 | Capacidad llena | Intento de inscribir cuando horario está lleno | Inscribir cuando capacidad=20 y hay 20 atletas | Toast error: "Este horario ha alcanzado su capacidad máxima." | Horario lleno | |
| TC-AS-04 | Atleta inexistente | Intento con atleta que no existe | Atleta: 999 | Toast error: "Atleta no encontrado." | | |

## FRONTEND - LISTAR ATLETAS EN HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-05 | Listar inscritos | Ver todos los atletas inscritos en un horario | Clic en horario | Tabla con columnas: Nombre Atleta, Email, Teléfono, Acciones (Remover). Ejemplo: Juan Perez \| juan@test.com \| 0999999999 \| Remover | Entrenador autenticado, Atletas registrados | |
| TC-AS-06 | Lista vacía | Sin atletas inscritos | Ver lista vacía | Mensaje: "No hay atletas registrados en este horario." Botón "Registrar Atleta" visible. | Sin inscritos | |

## FRONTEND - MARCAR ASISTENCIA

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-07 | Marcar asistencia presente | Marcar atleta como presente | Clic en checkbox "Presente" para atleta | Toast: "Asistencia registrada exitosamente." Checkbox marcado, guardado en BD. | Entrenador autenticado, Horario en progreso/pasado | |
| TC-AS-08 | Marcar asistencia ausente | Marcar atleta como ausente | Clic en checkbox "Ausente" para atleta | Toast: "Asistencia registrada exitosamente." Estado "Ausente" registrado. | | |
| TC-AS-09 | Ver historial asistencia | Ver registro histórico de asistencias de un atleta | Clic en "Historial" de atleta | Modal con tabla: Fecha, Horario, Estado (Presente/Ausente), Observaciones. Gráfico de asistencia (porcentaje). | Atleta con historial | |

## FRONTEND - REMOVER ATLETA

| ID | Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-10 | Remover atleta | Desincribir atleta de horario | Clic en "Remover" para atleta | Modal: "¿Deseas remover a este atleta del horario?" Confirmar. Toast: "Atleta removido exitosamente." Removido de tabla. | Entrenador autenticado, Atleta inscrito | |

---

## BACKEND - REGISTRAR ATLETA EN HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-01 | Registrar exitoso | POST /api/v1/entrenador/asistencias/registro | `{"atleta_id":1,"horario_id":1}` | `{"success":true,"message":"Atleta registrado en el horario exitosamente.","data":{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","atleta_id":1,"horario_id":1,"fecha_registro":"2026-01-20"},"errors":null}` (Status: 201) | Entrenador autenticado, Atleta y Horario existen | Exitoso |
| TC-AS-02 | Atleta ya inscrito | POST /api/v1/entrenador/asistencias/registro | `{"atleta_id":1,"horario_id":1}` | `{"success":false,"message":"El atleta ya está registrado en este horario.","data":null,"errors":null}` (Status: 409) | Atleta ya inscrito | Fallido |
| TC-AS-03 | Capacidad llena | POST /api/v1/entrenador/asistencias/registro | `{"atleta_id":5,"horario_id":1}` | `{"success":false,"message":"Este horario ha alcanzado su capacidad máxima.","data":null,"errors":null}` (Status: 409) | Horario lleno (20/20) | Fallido |
| TC-AS-04 | Atleta no encontrado | POST /api/v1/entrenador/asistencias/registro | `{"atleta_id":999,"horario_id":1}` | `{"success":false,"message":"Atleta no encontrado.","data":null,"errors":null}` (Status: 404) | Atleta no existe | Fallido |
| TC-AS-05 | Horario no encontrado | POST /api/v1/entrenador/asistencias/registro | `{"atleta_id":1,"horario_id":999}` | `{"success":false,"message":"Horario no encontrado.","data":null,"errors":null}` (Status: 404) | Horario no existe | Fallido |

---

## BACKEND - LISTAR ATLETAS EN HORARIO

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-06 | Listar atletas | GET /api/v1/entrenador/asistencias/horario/1 | (Sin body) | `{"success":true,"message":"Atletas en horario obtenidos exitosamente.","data":[{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","atleta_id":1,"atleta_nombre":"Juan Perez","atleta_email":"juan@test.com","atleta_telefono":"0999999999","horario_id":1,"fecha_registro":"2026-01-20"},{"id":2,"external_id":"660e8400-e29b-41d4-a716-446655440001","atleta_id":2,"atleta_nombre":"Maria Garcia","atleta_email":"maria@test.com","atleta_telefono":"0988888888","horario_id":1,"fecha_registro":"2026-01-20"}],"errors":null}` (Status: 200) | Entrenador autenticado, Atletas registrados | Exitoso |
| TC-AS-07 | Lista vacía | GET /api/v1/entrenador/asistencias/horario/1 | (Sin body) | `{"success":true,"message":"Atletas en horario obtenidos exitosamente.","data":[],"errors":null}` (Status: 200) | Sin atletas registrados | Exitoso |
| TC-AS-08 | Horario no encontrado | GET /api/v1/entrenador/asistencias/horario/999 | (Sin body) | `{"success":false,"message":"Horario no encontrado.","data":null,"errors":null}` (Status: 404) | Horario no existe | Fallido |

---

## BACKEND - MARCAR ASISTENCIA

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-09 | Marcar presente | POST /api/v1/entrenador/asistencias/registrar | `{"registro_asistencias_id":1,"estado":"PRESENTE","observaciones":"Participó activamente"}` | `{"success":true,"message":"Asistencia registrada exitosamente.","data":{"id":1,"external_id":"550e8400-e29b-41d4-a716-446655440000","registro_asistencias_id":1,"estado":"PRESENTE","observaciones":"Participó activamente","fecha":"2026-01-20"},"errors":null}` (Status: 201) | Entrenador autenticado, Registro existe | Exitoso |
| TC-AS-10 | Marcar ausente | POST /api/v1/entrenador/asistencias/registrar | `{"registro_asistencias_id":1,"estado":"AUSENTE","observaciones":"Justificado"}` | `{"success":true,"message":"Asistencia registrada exitosamente.","data":{"id":2,"external_id":"660e8400-e29b-41d4-a716-446655440001","registro_asistencias_id":1,"estado":"AUSENTE","observaciones":"Justificado","fecha":"2026-01-20"},"errors":null}` (Status: 201) | | Exitoso |
| TC-AS-11 | Registro no encontrado | POST /api/v1/entrenador/asistencias/registrar | `{"registro_asistencias_id":999,"estado":"PRESENTE","observaciones":""}` | `{"success":false,"message":"Registro de asistencia no encontrado.","data":null,"errors":null}` (Status: 404) | Registro no existe | Fallido |
| TC-AS-12 | Estado inválido | POST /api/v1/entrenador/asistencias/registrar | `{"registro_asistencias_id":1,"estado":"INVALID","observaciones":""}` | `{"success":false,"message":"Validation Error","data":null,"errors":[{"field":"estado","message":"Estado debe ser PRESENTE o AUSENTE"}]}` (Status: 422) | | Fallido |

---

## BACKEND - OBTENER HISTORIAL ASISTENCIA

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-13 | Obtener historial | GET /api/v1/entrenador/asistencias/registro/1/historial | (Sin body) | `{"success":true,"message":"Historial obtenido exitosamente.","data":{"registro_id":1,"atleta_nombre":"Juan Perez","asistencias":[{"id":1,"fecha":"2026-01-15","estado":"PRESENTE","observaciones":"Buena participación"},{"id":2,"fecha":"2026-01-17","estado":"AUSENTE","observaciones":"Justificado"}],"estadisticas":{"total":2,"presentes":1,"ausentes":1,"porcentaje_asistencia":50}},"errors":null}` (Status: 200) | Entrenador autenticado, Registro existe | Exitoso |
| TC-AS-14 | Registro no encontrado | GET /api/v1/entrenador/asistencias/registro/999/historial | (Sin body) | `{"success":false,"message":"Registro no encontrado.","data":null,"errors":null}` (Status: 404) | Registro no existe | Fallido |

---

## BACKEND - REMOVER ATLETA

| ID | Funcionalidad | Descripción | Datos de Entrada (JSON) | Salida Esperada (JSON) | Condiciones Previas | Resultado (Exitoso/Fallido) |
|---|---|---|---|---|---|---|
| TC-AS-15 | Remover exitoso | DELETE /api/v1/entrenador/asistencias/registro/1 | (Sin body) | `{"success":true,"message":"Atleta removido del horario exitosamente.","data":null,"errors":null}` (Status: 200) | Entrenador autenticado, Registro existe | Exitoso |
| TC-AS-16 | Registro no encontrado | DELETE /api/v1/entrenador/asistencias/registro/999 | (Sin body) | `{"success":false,"message":"Registro no encontrado.","data":null,"errors":null}` (Status: 404) | Registro no existe | Fallido |
| TC-AS-17 | Sin permisos | DELETE /api/v1/entrenador/asistencias/registro/1 (pertenece a otro entrenador) | (Sin body) | `{"success":false,"message":"No tienes permiso para remover este atleta.","data":null,"errors":null}` (Status: 403) | Registro pertenece a otro entrenador | Fallido |

---

# NOTAS TÉCNICAS GLOBALES

## APIResponse - Estructura Estándar
Todos los endpoints deben retornar una respuesta con esta estructura:
```json
{
  "success": true/false,
  "message": "Mensaje descriptivo",
  "data": {},
  "errors": null
}
```

## Códigos HTTP
- **200** - OK (GET exitoso)
- **201** - Created (POST exitoso)
- **204** - No Content (DELETE exitoso)
- **400** - Bad Request (Validación fallida)
- **403** - Forbidden (Sin permisos)
- **404** - Not Found (Recurso no existe)
- **409** - Conflict (Duplicado, capacidad llena, etc)
- **422** - Unprocessable Entity (Errores de validación)

## Estados de Asistencia
- `PRESENTE` - Atleta asistió
- `AUSENTE` - Atleta no asistió

## Disciplinas Permitidas
- `ATLETISMO`
- `NATACION`
- `FUTBOL`
- `BALONCESTO`
- `VOLLEYBALL`

## Niveles Permitidos
- `PRINCIPIANTE`
- `INTERMEDIO`
- `AVANZADO`

---

# CHECKLIST DE IMPLEMENTACIÓN

## Fase 1: Casos de Prueba ✅
- [x] Casos de prueba Frontend completados
- [x] Casos de prueba Backend completados
- [x] Todos los JSON son 100% válidos y completos
- [x] Ningún placeholder (...) o valores implícitos
- [x] Contratos claros entre Frontend y Backend

## Fase 2: Frontend
- [ ] Componentes creados para Entrenamiento
- [ ] Componentes creados para Horario
- [ ] Componentes creados para Asistencia
- [ ] Toasts implementados para todos los mensajes
- [ ] Validaciones implementadas
- [ ] No hay errores silenciosos

## Fase 3: Backend
- [ ] Servicios implementados (entrenamiento_service.py, asistencia_service.py)
- [ ] Routers implementados
- [ ] APIResponse utilizado en todas las respuestas
- [ ] Validaciones de negocio implementadas
- [ ] Manejo de errores completo

## Fase 4: Verificación
- [ ] Tests creados para todos los casos
- [ ] Frontend y Backend alineados
- [ ] Mensajes coinciden exactamente
- [ ] JSONs son idénticos entre casos de prueba y código
- [ ] Proyecto listo para QA

