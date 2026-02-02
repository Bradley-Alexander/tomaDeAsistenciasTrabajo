## CU-005: Listado de usuarios
| Campo | Descripción |---|
|---|---|---|
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
