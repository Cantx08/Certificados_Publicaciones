""" Configuración de la base de datos """

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno (busca el .env en la raíz o carpeta actual)
load_dotenv()

# Construir la URL de conexión usando las variables del .env
# OJO: Si estás corriendo esto LOCAL (fuera de docker), el host es 'localhost'
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST") # Porque nos conectamos desde afuera del contenedor
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para crear los modelos más adelante
Base = declarative_base()

# Dependencia para obtener la DB en los endpoints
def get_db():
    """ Proveer una sesión de base de datos. """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
