from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str] = None

class ClienteUpdate(BaseModel):
    nombre: Optional[str]
    email: Optional[str]
    telefono: Optional[str]

class Proyecto(BaseModel):
    cliente_id: int
    nombre: str
    descripcion: Optional[str] = None

class ProyectoUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
