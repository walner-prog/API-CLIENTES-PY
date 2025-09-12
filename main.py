from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import sqlite3

app = FastAPI(title="Mini CG Sistema API")

# Conexión SQLite
conn = sqlite3.connect("clientes.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT,
    fecha_creacion TEXT
)
""")
conn.commit()

# Modelos Pydantic
class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str] = None

class ClienteUpdate(BaseModel):
    nombre: Optional[str]
    email: Optional[str]
    telefono: Optional[str]

# CRUD Endpoints
@app.post("/clientes/", response_model=dict)
def crear_cliente(cliente: Cliente):
    fecha = datetime.now().isoformat()
    cursor.execute("INSERT INTO clientes (nombre, email, telefono, fecha_creacion) VALUES (?, ?, ?, ?)",
                   (cliente.nombre, cliente.email, cliente.telefono, fecha))
    conn.commit()
    return {"id": cursor.lastrowid, "nombre": cliente.nombre, "email": cliente.email, "telefono": cliente.telefono}

@app.get("/clientes/", response_model=List[dict])
def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    return [{"id": r[0], "nombre": r[1], "email": r[2], "telefono": r[3], "fecha_creacion": r[4]} for r in rows]

@app.get("/clientes/{cliente_id}", response_model=dict)
def obtener_cliente(cliente_id: int):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (cliente_id,))
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "nombre": row[1], "email": row[2], "telefono": row[3], "fecha_creacion": row[4]}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.put("/clientes/{cliente_id}", response_model=dict)
def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (cliente_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    nombre = cliente.nombre or row[1]
    email = cliente.email or row[2]
    telefono = cliente.telefono or row[3]
    cursor.execute("UPDATE clientes SET nombre=?, email=?, telefono=? WHERE id=?",
                   (nombre, email, telefono, cliente_id))
    conn.commit()
    return {"id": cliente_id, "nombre": nombre, "email": email, "telefono": telefono}

@app.delete("/clientes/{cliente_id}", response_model=dict)
def eliminar_cliente(cliente_id: int):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (cliente_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    cursor.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
    conn.commit()
    return {"detail": f"Cliente {cliente_id} eliminado"}
