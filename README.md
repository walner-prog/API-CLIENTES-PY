# Gestion Clientes-proyectos API

API rápida para la **gestión de clientes y proyectos**. CRUD completo desarrollado en **Python (FastAPI)** con almacenamiento en **SQLite**, utilizando arquitectura modular (`models`, `services`, `controllers`, `routes`).

---

## 🔧 Tecnologías
- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- Swagger UI (incluido con FastAPI)



# 📄 Endpoints principales

## Clientes

- `POST /clientes/` – Crear cliente
- `GET /clientes/` – Listar todos los clientes
- `GET /clientes/{id}` – Obtener cliente por ID
- `PUT /clientes/{id}` – Actualizar cliente
- `DELETE /clientes/{id}` – Eliminar cliente

## Proyectos

- `POST /proyectos/` – Crear proyecto (opcional asociar a cliente)
- `GET /proyectos/` – Listar todos los proyectos o por cliente
- `PUT /proyectos/{id}` – Actualizar proyecto
- `DELETE /proyectos/{id}` – Eliminar proyecto

---

# 🏗️ Arquitectura

- `main.py` – Inicialización de FastAPI y rutas
- `app/routes.py` – Router y definición de endpoints
- `app/controllers.py` – Controladores que llaman a los servicios
- `app/services.py` – Lógica de negocio y acceso a base de datos
- `app/models.py` – Modelos Pydantic para validación
- `app/database.py` – Conexión SQLite y creación de tablas


---
mini-cg-sistema/
│
├─ main.py
├─ app/
│  ├─ __init__.py
│  ├─ routes.py
│  ├─ controllers.py
│  ├─ services.py
│  ├─ models.py
│  └─ database.py
└─ README.md


