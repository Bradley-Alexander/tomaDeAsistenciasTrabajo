# 📚 Documentación Completa - Tests de Router de Horarios (Entrenador)

## 🎯 Resumen General
Este documento contiene la documentación detallada de los tests para el módulo de gestión de horarios de entrenamientos para entrenadores, incluyendo tablas para Backend y Frontend con todos los casos de éxito y fallo.

---

# 📋 PARTE 1: TABLA BACKEND

## CREATE HORARIO - CREAR EXITOSO

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Crear horario válido |
| **Descripción** | Creación de un nuevo horario de entrenamiento con datos válidos |
| **Endpoint** | POST `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` |
| **Datos de Entrada (JSON)** | `{"name": "Entrenamiento Matutino", "hora_inicio": "08:00:00", "hora_fin": "10:00:00"}` |
| **Salida Esperada (JSON)** | `{"id": 1, "external_id": "uuid", "name": "Entrenamiento Matutino", "hora_inicio": "08:00:00", "hora_fin": "10:00:00", "entrenamiento_id": 1}` |
| **Status Code** | 201 Created |
| **Condiciones Previas** | Entrenador autenticado, Entrenamiento existente, Entrenador autorizado para el entrenamiento |
| **Resultado** | ✅ EXITOSO |

---

## CREATE HORARIO - ENTRENAMIENTO NO ENCONTRADO

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Crear horario con entrenamiento inexistente |
| **Descripción** | Intento de crear un horario para un entrenamiento que no existe o no está autorizado |
| **Endpoint** | POST `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` |
| **Datos de Entrada (JSON)** | `{"name": "Entrenamiento Matutino", "hora_inicio": "08:00:00", "hora_fin": "10:00:00"}` |
| **Salida Esperada (JSON)** | `{"detail": "Entrenamiento no encontrado o no autorizado"}` |
| **Status Code** | 404 Not Found |
| **Condiciones Previas** | Entrenador autenticado, Entrenamiento NO existe o no autorizado |
| **Resultado** | ✅ FALLIDO |

---

## CREATE HORARIO - HORAS INVÁLIDAS

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Crear horario con horas inválidas |
| **Descripción** | Intento de crear un horario donde la hora de inicio es >= hora de fin |
| **Endpoint** | POST `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` |
| **Datos de Entrada (JSON)** | `{"name": "Entrenamiento Inválido", "hora_inicio": "10:00:00", "hora_fin": "08:00:00"}` |
| **Salida Esperada (JSON)** | `{"detail": "La hora de inicio debe ser anterior a la hora de fin"}` |
| **Status Code** | 400 Bad Request |
| **Condiciones Previas** | Entrenador autenticado, Entrenamiento existente, Horas en formato incorrecto |
| **Resultado** | ✅ FALLIDO |

---

## GET HORARIOS - OBTENER EXITOSO

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Obtener horarios de un entrenamiento |
| **Descripción** | Obtener lista de todos los horarios asociados a un entrenamiento específico |
| **Endpoint** | GET `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` |
| **Datos de Entrada** | `entrenamiento_id: 1` |
| **Salida Esperada (JSON)** | `[{"id": 1, "external_id": "uuid", "entrenamiento_id": 1, "name": "Entrenamiento Vespertino", "hora_inicio": "16:00:00", "hora_fin": "18:00:00"}]` |
| **Status Code** | 200 OK |
| **Condiciones Previas** | Entrenador autenticado, Entrenamiento existente, Horarios creados |
| **Resultado** | ✅ EXITOSO |

---

## GET HORARIOS - ENTRENAMIENTO NO ENCONTRADO

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Obtener horarios de entrenamiento inexistente |
| **Descripción** | Intento de obtener horarios de un entrenamiento que no existe o no está autorizado |
| **Endpoint** | GET `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` |
| **Datos de Entrada** | `entrenamiento_id: 999` |
| **Salida Esperada (JSON)** | `{"detail": "Entrenamiento no encontrado o no autorizado"}` |
| **Status Code** | 404 Not Found |
| **Condiciones Previas** | Entrenador autenticado, Entrenamiento NO existe o no autorizado |
| **Resultado** | ✅ FALLIDO |

---

## GET HORARIOS - LISTA VACÍA

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Obtener horarios cuando no existen |
| **Descripción** | Obtener lista de horarios cuando el entrenamiento no tiene horarios registrados |
| **Endpoint** | GET `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` |
| **Datos de Entrada** | `entrenamiento_id: 1` |
| **Salida Esperada (JSON)** | `[]` (lista vacía) |
| **Status Code** | 200 OK |
| **Condiciones Previas** | Entrenador autenticado, Entrenamiento existente, Sin horarios registrados |
| **Resultado** | ✅ EXITOSO |

---

## DELETE HORARIO - ELIMINAR EXITOSO

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Eliminar horario existente |
| **Descripción** | Eliminación de un horario específico que pertenece al entrenador autenticado |
| **Endpoint** | DELETE `/api/v1/entrenador/horarios/{id}` |
| **Datos de Entrada** | `horario_id: 1` |
| **Salida Esperada (JSON)** | Sin contenido (respuesta vacía) |
| **Status Code** | 204 No Content |
| **Condiciones Previas** | Entrenador autenticado, Horario existente, Entrenador autorizado (propietario del horario) |
| **Resultado** | ✅ EXITOSO |

---

## DELETE HORARIO - HORARIO NO ENCONTRADO

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Eliminar horario inexistente |
| **Descripción** | Intento de eliminar un horario que no existe |
| **Endpoint** | DELETE `/api/v1/entrenador/horarios/{id}` |
| **Datos de Entrada** | `horario_id: 999` |
| **Salida Esperada (JSON)** | `{"detail": "Horario no encontrado"}` |
| **Status Code** | 404 Not Found |
| **Condiciones Previas** | Entrenador autenticado, Horario NO existe |
| **Resultado** | ✅ FALLIDO |

---

## DELETE HORARIO - SIN PERMISOS

| Parámetro | Valor |
|-----------|-------|
| **Funcionalidad** | Eliminar horario sin autorización |
| **Descripción** | Intento de eliminar un horario que pertenece a otro entrenador (sin permisos) |
| **Endpoint** | DELETE `/api/v1/entrenador/horarios/{id}` |
| **Datos de Entrada** | `horario_id: 1` |
| **Salida Esperada (JSON)** | `{"detail": "No tienes permiso para eliminar este horario"}` |
| **Status Code** | 403 Forbidden |
| **Condiciones Previas** | Entrenador autenticado (diferente al propietario), Horario existente pero pertenece a otro entrenador |
| **Resultado** | ✅ FALLIDO |

---

# 🎨 PARTE 2: TABLA FRONTEND

## CREATE HORARIO - CREAR EXITOSO

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Crear horario válido |
| **Descripción** | Formulario para crear un nuevo horario de entrenamiento con todos los campos obligatorios y válidos |
| **Datos de Entrada (Formulario)** | **Nombre:** Entrenamiento Matutino<br/>**Hora Inicio:** 08:00<br/>**Hora Fin:** 10:00 |
| **Salida Esperada** | **Mensaje:** "Horario creado exitosamente"<br/>**Acción:** Actualizar lista de horarios, cerrar modal/formulario |
| **Condiciones Previas** | Usuario autenticado como entrenador, Entrenamiento seleccionado existe, API disponible |
| **Resultado** | ✅ EXITOSO |

---

## CREATE HORARIO - ENTRENAMIENTO NO ENCONTRADO

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Crear horario con entrenamiento inválido |
| **Descripción** | Intento de crear un horario cuando el entrenamiento no existe o no tiene autorización |
| **Datos de Entrada (Formulario)** | **Nombre:** Entrenamiento Matutino<br/>**Hora Inicio:** 08:00<br/>**Hora Fin:** 10:00 |
| **Salida Esperada** | **Mensaje de Error:** "Entrenamiento no encontrado o no autorizado"<br/>**Acción:** Mantener formulario visible, mostrar alerta roja |
| **Condiciones Previas** | Usuario autenticado como entrenador, Entrenamiento no existe o no está autorizado, API disponible |
| **Resultado** | ✅ FALLIDO |

---

## CREATE HORARIO - HORAS INVÁLIDAS

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Crear horario con horas inválidas |
| **Descripción** | Formulario intenta crear un horario donde la hora de inicio es >= hora de fin |
| **Datos de Entrada (Formulario)** | **Nombre:** Entrenamiento Inválido<br/>**Hora Inicio:** 10:00<br/>**Hora Fin:** 08:00 |
| **Salida Esperada** | **Mensaje de Error:** "La hora de inicio debe ser anterior a la hora de fin"<br/>**Acción:** Mantener formulario visible, destacar campos de horas con borde rojo |
| **Condiciones Previas** | Usuario autenticado como entrenador, Validación en frontend o backend falla, API disponible |
| **Resultado** | ✅ FALLIDO |

---

## GET HORARIOS - OBTENER EXITOSO

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Obtener lista de horarios |
| **Descripción** | Carga y visualización de todos los horarios asociados a un entrenamiento específico |
| **Datos de Entrada** | Seleccionar entrenamiento de la lista desplegable |
| **Salida Esperada** | **Tabla/Lista:** Mostrar horarios con columnas: Nombre, Hora Inicio, Hora Fin, Acciones (Editar/Eliminar)<br/>**Ejemplo:**<br/>- Entrenamiento Vespertino \| 16:00 \| 18:00 \| Editar \| Eliminar |
| **Condiciones Previas** | Usuario autenticado como entrenador, Entrenamiento seleccionado existe, Horarios creados en BD |
| **Resultado** | ✅ EXITOSO |

---

## GET HORARIOS - LISTA VACÍA

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Obtener horarios cuando no existen |
| **Descripción** | Vista cuando el entrenamiento no tiene horarios registrados |
| **Datos de Entrada** | Seleccionar entrenamiento sin horarios |
| **Salida Esperada** | **Mensaje Informativo:** "No hay horarios registrados para este entrenamiento"<br/>**Acción:** Mostrar botón "Crear nuevo horario" |
| **Condiciones Previas** | Usuario autenticado como entrenador, Entrenamiento sin horarios, API disponible |
| **Resultado** | ✅ EXITOSO |

---

## GET HORARIOS - ENTRENAMIENTO NO ENCONTRADO

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Obtener horarios de entrenamiento inexistente |
| **Descripción** | Intento de cargar horarios cuando el entrenamiento no existe o el usuario no está autorizado |
| **Datos de Entrada** | URL con `entrenamiento_id` inválido o no autorizado |
| **Salida Esperada** | **Mensaje de Error:** "Entrenamiento no encontrado o no autorizado"<br/>**Acción:** Mostrar alerta roja, redirigir a lista de entrenamientos |
| **Condiciones Previas** | Usuario autenticado como entrenador, Entrenamiento no existe o no autorizado, API disponible |
| **Resultado** | ✅ FALLIDO |

---

## DELETE HORARIO - ELIMINAR EXITOSO

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Eliminar horario |
| **Descripción** | Eliminación de un horario específico con confirmación del usuario |
| **Datos de Entrada** | Clic en botón "Eliminar" para un horario, confirmar acción |
| **Salida Esperada** | **Mensaje:** "Horario eliminado exitosamente"<br/>**Acción:** Remover horario de la lista, actualizar tabla |
| **Condiciones Previas** | Usuario autenticado como entrenador, Horario seleccionado existe, Usuario es propietario del horario, API disponible |
| **Resultado** | ✅ EXITOSO |

---

## DELETE HORARIO - HORARIO NO ENCONTRADO

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Eliminar horario inexistente |
| **Descripción** | Intento de eliminar un horario que no existe |
| **Datos de Entrada** | ID de horario inválido en URL o parámetro |
| **Salida Esperada** | **Mensaje de Error:** "Horario no encontrado"<br/>**Acción:** Mostrar alerta roja, mantener lista visible |
| **Condiciones Previas** | Usuario autenticado como entrenador, Horario NO existe en BD, API disponible |
| **Resultado** | ✅ FALLIDO |

---

## DELETE HORARIO - SIN PERMISOS

| Elemento | Contenido |
|----------|-----------|
| **Funcionalidad** | Intentar eliminar horario de otro entrenador |
| **Descripción** | Intento de eliminar un horario que pertenece a otro entrenador (sin autorización) |
| **Datos de Entrada** | Clic en botón "Eliminar" para horario ajeno, confirmar acción |
| **Salida Esperada** | **Mensaje de Error:** "No tienes permiso para eliminar este horario"<br/>**Acción:** Mostrar alerta naranja/roja, bloquear eliminar, ocultar botón |
| **Condiciones Previas** | Usuario autenticado como entrenador diferente, Horario existe pero pertenece a otro entrenador, API disponible |
| **Resultado** | ✅ FALLIDO |

---

# 📊 PARTE 3: RESUMEN DE EJECUCIÓN

```
Fecha: 20/01/2026
Framework: pytest + pytest-asyncio
Total de Tests: 9
Passed: 9 ✅
Failed: 0
Warnings: 32 (Pydantic deprecation warnings - no afecta funcionalidad)
Tiempo Total: 0.91s

Cobertura de Funcionalidades:
├─ Create Horario: 3 casos (1 éxito, 2 fallos)
├─ Get Horarios: 3 casos (2 éxito, 1 fallo)
└─ Delete Horario: 3 casos (1 éxito, 2 fallos)
```

---

# 🔍 PARTE 4: REFERENCIA RÁPIDA

## Códigos de Estado HTTP

| Status | Significado | Casos de Uso |
|--------|------------|--------------|
| 200 | OK | GET horarios exitoso, lista vacía |
| 201 | Created | POST horario exitoso |
| 204 | No Content | DELETE horario exitoso |
| 400 | Bad Request | Validación de entrada fallida (horas inválidas) |
| 403 | Forbidden | Usuario sin permisos para la acción |
| 404 | Not Found | Recurso no encontrado (entrenamiento, horario) |

---

## Mensajes de Error del Backend

| Código | Mensaje | Causa |
|--------|---------|-------|
| 400 | "La hora de inicio debe ser anterior a la hora de fin" | Validación de rango de horas falló |
| 404 | "Entrenamiento no encontrado o no autorizado" | Entrenamiento no existe o no pertenece al entrenador |
| 404 | "Horario no encontrado" | Horario no existe en BD |
| 403 | "No tienes permiso para eliminar este horario" | Horario pertenece a otro entrenador |

---

## Flujos de Usuario en Frontend

### Flujo Exitoso de Crear Horario
1. Entrenador accede a módulo de horarios
2. Selecciona entrenamiento
3. Hace clic en "Crear nuevo horario"
4. Completa formulario (Nombre, Hora Inicio, Hora Fin)
5. Hace clic en "Guardar"
6. Sistema valida en frontend y backend
7. **Mensaje:** "Horario creado exitosamente"
8. Lista se actualiza automáticamente

### Flujo Exitoso de Obtener Horarios
1. Entrenador selecciona un entrenamiento
2. Sistema carga lista de horarios
3. Se muestra tabla con todos los horarios
4. Cada fila tiene botones de Editar/Eliminar

### Flujo Exitoso de Eliminar Horario
1. Entrenador hace clic en "Eliminar" en un horario
2. Sistema muestra confirmación
3. Usuario confirma acción
4. Sistema elimina horario
5. **Mensaje:** "Horario eliminado exitosamente"
6. Tabla se actualiza

---

## 📝 Notas Técnicas

- **Autenticación:** Todos los endpoints requieren usuario entrenador autenticado
- **Validación de Horas:** `hora_inicio` < `hora_fin` (obligatorio)
- **Autorización:** Se verifica que el entrenador sea propietario del entrenamiento/horario
- **Mocking:** Tests utilizan mocks para simular servicios y dependencias
- **Fixtures:** `client` (AsyncClient), `mock_horario_service`
- **Patrón de Testing:** AAA (Arrange, Act, Assert)

---

## 🧪 Estrategia de Testing

1. **Unit Tests:** Cada método del servicio se prueba de forma aislada
2. **Integration Tests:** Endpoints se prueban a través del cliente HTTP
3. **Mock Strategy:** Se mockean las dependencias de base de datos y servicios
4. **Validación Completa:** Se prueban casos de éxito y todos los casos de error

---

## ✅ Checklist de Pruebas

- [x] Crear horario con datos válidos
- [x] Crear horario con entrenamiento inexistente (404)
- [x] Crear horario con horas inválidas (400)
- [x] Obtener horarios de un entrenamiento
- [x] Obtener horarios cuando lista está vacía
- [x] Obtener horarios de entrenamiento inexistente (404)
- [x] Eliminar horario existente
- [x] Eliminar horario inexistente (404)
- [x] Eliminar horario sin permisos (403)

