# Documentación de Tests - Router de Horarios (Entrenador)

## Resumen General
Este módulo de pruebas verifica los endpoints de gestión de horarios para entrenadores, validando operaciones de creación, obtención y eliminación de horarios de entrenamiento.

---

## Tabla de Pruebas

| Funcionalidad | Descripción | Datos de Entrada | Salida Esperada | Condiciones Previas | Resultado |
|---|---|---|---|---|---|
| **test_create_horario** | Verifica la creación de un nuevo horario de entrenamiento mediante una solicitud POST | Payload JSON:<br/>- `name`: "Entrenamiento Matutino"<br/>- `hora_inicio`: "08:00:00"<br/>- `hora_fin`: "10:00:00"<br/>- `entrenamiento_id`: 1 | - Status code: 201<br/>- Response contiene `name`: "Entrenamiento Matutino"<br/>- Método `create_horario` fue llamado una vez | - Cliente AsyncClient disponible<br/>- Mock de `HorarioService` configurado<br/>- Dependencias de `get_horario_service` y `get_current_entrenador` mocked<br/>- Usuario entrenador autenticado (mock con id=1, usuario_id=1) | ✅ PASSED |
| **test_get_horarios_by_entrenamiento** | Verifica la obtención de horarios asociados a un entrenamiento específico mediante GET | - `entrenamiento_id`: 1<br/>- Sin body en la solicitud | - Status code: 200<br/>- Response es una lista con 1 elemento<br/>- Primer elemento tiene `name`: "Entrenamiento Vespertino" | - Cliente AsyncClient disponible<br/>- Mock de `HorarioService` configurado<br/>- Dependencias de `get_horario_service` y `get_current_entrenador` mocked<br/>- Usuario entrenador autenticado (mock con id=1, usuario_id=1)<br/>- Horarios existentes en el mock | ✅ PASSED |
| **test_delete_horario** | Verifica la eliminación de un horario específico mediante una solicitud DELETE | - `horario_id`: 1<br/>- Sin body en la solicitud | - Status code: 204 (No Content)<br/>- Método `delete_horario` fue llamado una vez | - Cliente AsyncClient disponible<br/>- Mock de `HorarioService` configurado<br/>- Dependencias de `get_horario_service` y `get_current_entrenador` mocked<br/>- Usuario entrenador autenticado (mock con id=1, usuario_id=1)<br/>- Horario existente a eliminar | ✅ PASSED |

---

## Detalles Técnicos

### Configuración Común
- **Framework de Testing**: pytest con soporte asincrónico (pytest-asyncio)
- **Cliente HTTP**: httpx.AsyncClient
- **Mocking**: unittest.mock (AsyncMock, MagicMock)
- **Endpoints Base**: `/api/v1/entrenador/horarios/`

### Fixtures Utilizadas
- `client`: Fixture que proporciona un cliente HTTP asincrónico configurado para hacer solicitudes a la aplicación FastAPI
- `mock_horario_service`: Fixture que retorna un mock del servicio de horarios

### Dependencias Mocked
- `get_horario_service`: Devuelve el mock del servicio de horarios
- `get_current_entrenador`: Devuelve un mock de entrenador con `id=1` y `usuario_id=1`

### Patrones de Override
Cada test utiliza `_APP.dependency_overrides` para reemplazar las dependencias reales con sus versiones mockadas, y limpia los overrides al finalizar.

---

## Endpoints Probados

| Método | Endpoint | Test | Estado |
|--------|----------|------|--------|
| POST | `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` | test_create_horario | ✅ |
| GET | `/api/v1/entrenador/horarios/entrenamiento/{entrenamiento_id}` | test_get_horarios_by_entrenamiento | ✅ |
| DELETE | `/api/v1/entrenador/horarios/{id}` | test_delete_horario | ✅ |

---

## Resumen de Ejecución

```
Fecha: 20/01/2026
Total de Tests: 3
Passed: 3 ✅
Failed: 0
Warnings: 32 (Pydantic deprecation warnings - no afectan los tests)
Tiempo Total: 0.38s
```

### Observaciones
- Todos los tests pasaron exitosamente
- Las advertencias son relacionadas con deprecaciones en Pydantic v2 (uso de `required` en lugar de `json_schema_extra`)
- No hay impacto en la funcionalidad de los tests
- Los mocks están correctamente configurados
