# app/main.py
from fastapi import FastAPI
from gumigest_app.api.v1 import user
import gumigest_app.models
from gumigest_app.core.database import Base, engine

app = FastAPI()

# Crear tablas al arrancar
Base.metadata.create_all(bind=engine)
app.include_router(user.router)
