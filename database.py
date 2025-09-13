import sqlite3

conn = sqlite3.connect("clientes.db", check_same_thread=False)
cursor = conn.cursor()

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT,
    fecha_creacion TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS proyectos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    fecha_creacion TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
""")
conn.commit()
