""" Módulo principal de la aplicación """

from fastapi import FastAPI
from app.database import engine, Base

# Crear las tablas (esto es temporal, luego lo hará Alembic, pero sirve para probar conexión)
# Base.metadata.create_all(bind=engine) 

app = FastAPI(title="Certificación de publicaciones EPN")

@app.get("/health")
def health_check():
    """ Verifica que la API está ejecutándose correctamente"""
    return {"status": "ok", "message": "La API es corriendo correctamente."}
