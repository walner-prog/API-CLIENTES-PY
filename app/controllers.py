from . import services
from .models import Cliente, ClienteUpdate, Proyecto, ProyectoUpdate
from fastapi import HTTPException


# Clientes
def crear_cliente_controller(cliente: Cliente):
    id = services.crear_cliente(cliente)
    return {"id": id, **cliente.dict()}

def listar_clientes_controller():
    return services.listar_clientes()

def obtener_cliente_controller(cliente_id: int):
    cliente = services.obtener_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

def actualizar_cliente_controller(cliente_id: int, cliente: ClienteUpdate):
    updated = services.actualizar_cliente(cliente_id, cliente)
    if not updated:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return updated

def eliminar_cliente_controller(cliente_id: int):
    services.eliminar_cliente(cliente_id)
    return {"detail": f"Cliente {cliente_id} eliminado"}

# Proyectos
def crear_proyecto_controller(proyecto: Proyecto):
    id = services.crear_proyecto(proyecto)
    return {"id": id, **proyecto.dict()}

def listar_proyectos_controller(cliente_id: int = None):
    return services.listar_proyectos(cliente_id)

def actualizar_proyecto_controller(proyecto_id: int, proyecto: ProyectoUpdate):
    updated = services.actualizar_proyecto(proyecto_id, proyecto)
    if not updated:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return updated

def eliminar_proyecto_controller(proyecto_id: int):
    services.eliminar_proyecto(proyecto_id)
    return {"detail": f"Proyecto {proyecto_id} eliminado"}
