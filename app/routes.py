from fastapi import APIRouter
from . import controllers
from .models import Cliente, ClienteUpdate, Proyecto, ProyectoUpdate


router = APIRouter()

# Clientes
router.post("/clientes/")(controllers.crear_cliente_controller)
router.get("/clientes/")(controllers.listar_clientes_controller)
router.get("/clientes/{cliente_id}")(controllers.obtener_cliente_controller)
router.put("/clientes/{cliente_id}")(controllers.actualizar_cliente_controller)
router.delete("/clientes/{cliente_id}")(controllers.eliminar_cliente_controller)

# Proyectos
router.post("/proyectos/")(controllers.crear_proyecto_controller)
router.get("/proyectos/")(controllers.listar_proyectos_controller)
router.put("/proyectos/{proyecto_id}")(controllers.actualizar_proyecto_controller)
router.delete("/proyectos/{proyecto_id}")(controllers.eliminar_proyecto_controller)
