from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Mini CG Sistema API - Modular")
app.include_router(router)

