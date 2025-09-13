from .models import Cliente, ClienteUpdate, Proyecto, ProyectoUpdate
from database import conn
from datetime import datetime
from typing import List


cursor = conn.cursor()

# ----- CLIENTES -----
def crear_cliente(cliente: Cliente):
    fecha = datetime.now().isoformat()
    cursor.execute("INSERT INTO clientes (nombre, email, telefono, fecha_creacion) VALUES (?, ?, ?, ?)",
                   (cliente.nombre, cliente.email, cliente.telefono, fecha))
    conn.commit()
    return cursor.lastrowid

def listar_clientes() -> List[dict]:
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    return [{"id": r[0], "nombre": r[1], "email": r[2], "telefono": r[3], "fecha_creacion": r[4]} for r in rows]

def obtener_cliente(cliente_id: int) -> dict:
    cursor.execute("SELECT * FROM clientes WHERE id=?", (cliente_id,))
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "nombre": row[1], "email": row[2], "telefono": row[3], "fecha_creacion": row[4]}
    return None

def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate):
    existing = obtener_cliente(cliente_id)
    if not existing:
        return None
    nombre = cliente.nombre or existing["nombre"]
    email = cliente.email or existing["email"]
    telefono = cliente.telefono or existing["telefono"]
    cursor.execute("UPDATE clientes SET nombre=?, email=?, telefono=? WHERE id=?",
                   (nombre, email, telefono, cliente_id))
    conn.commit()
    return {"id": cliente_id, "nombre": nombre, "email": email, "telefono": telefono}

def eliminar_cliente(cliente_id: int):
    cursor.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
    conn.commit()

# ----- PROYECTOS -----
def crear_proyecto(proyecto: Proyecto):
    fecha = datetime.now().isoformat()
    cursor.execute("INSERT INTO proyectos (cliente_id, nombre, descripcion, fecha_creacion) VALUES (?, ?, ?, ?)",
                   (proyecto.cliente_id, proyecto.nombre, proyecto.descripcion, fecha))
    conn.commit()
    return cursor.lastrowid

def listar_proyectos(cliente_id: int = None) -> List[dict]:
    if cliente_id:
        cursor.execute("SELECT * FROM proyectos WHERE cliente_id=?", (cliente_id,))
    else:
        cursor.execute("SELECT * FROM proyectos")
    rows = cursor.fetchall()
    return [{"id": r[0], "cliente_id": r[1], "nombre": r[2], "descripcion": r[3], "fecha_creacion": r[4]} for r in rows]

def actualizar_proyecto(proyecto_id: int, proyecto: ProyectoUpdate):
    cursor.execute("SELECT * FROM proyectos WHERE id=?", (proyecto_id,))
    row = cursor.fetchone()
    if not row:
        return None
    nombre = proyecto.nombre or row[2]
    descripcion = proyecto.descripcion or row[3]
    cursor.execute("UPDATE proyectos SET nombre=?, descripcion=? WHERE id=?",
                   (nombre, descripcion, proyecto_id))
    conn.commit()
    return {"id": proyecto_id, "nombre": nombre, "descripcion": descripcion}

def eliminar_proyecto(proyecto_id: int):
    cursor.execute("DELETE FROM proyectos WHERE id=?", (proyecto_id,))
    conn.commit()
